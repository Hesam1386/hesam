
from pathlib import Path
from django.conf import settings
from movies.models import Film
import shutil

slugs = [
    "dune", "batman-the-dark-knight", "fight-club", "mother",
    "3-iron", "the-lobster", "oldboy", "ex-machina",
    "shutter-island", "leon-the-professional", "the-handmaiden",
    "black-swan", "upgrade", "parasite", "knives-out",
    "before-trilogy", "pulp-fiction", "the-platform-1-2",
    "inglourious-basterds", "the-lord-of-the-rings", "mud",
    "society-of-the-snow", "dont-look-up", "there-will-be-blood",
    "pieces-of-a-woman", "memento", "wild-tales", "bugonia",
    "speak-no-evil", "21-grams", "birdman",
    "the-shawshank-redemption", "amores-perros", "her",
    "gone-girl", "one-flew-over-the-cuckoos-nest",
    "the-pursuit-of-happyness", "memories-of-murder",
    "room", "nuremberg",
]

extensions = {".jpg", ".jpeg", ".png", ".webp"}

poster_source = Path(r"D:\posters")
backdrop_source = Path(r"D:\photo site")

poster_target = Path(settings.MEDIA_ROOT) / "posters"
backdrop_target = Path(settings.MEDIA_ROOT) / "backdrops"

# ابتدا همه تصاویر را بررسی می‌کنیم
plans = []

for number, slug in enumerate(slugs, start=1):
    film = Film.objects.get(slug=slug)

    posters = [
        p for p in (poster_source / f"movie_{number:02d}").rglob("*")
        if p.is_file() and p.suffix.lower() in extensions
    ]

    backdrops = [
        p for p in (backdrop_source / f"movie_{number:02d}").rglob("*")
        if p.is_file() and p.suffix.lower() in extensions
    ]

    if len(posters) != 1 or len(backdrops) != 1:
        raise ValueError(f"Image problem: {film.title}")

    plans.append((film, posters[0], backdrops[0]))

if len(plans) != 40:
    raise ValueError("Expected exactly 40 films.")

# ساخت پوشه‌های مقصد
poster_target.mkdir(parents=True, exist_ok=True)
backdrop_target.mkdir(parents=True, exist_ok=True)

# کپی تصاویر و اتصال به دیتابیس
for film, poster, backdrop in plans:
    poster_name = f"{film.slug}{poster.suffix.lower()}"
    backdrop_name = f"{film.slug}{backdrop.suffix.lower()}"

    shutil.copy2(poster, poster_target / poster_name)
    shutil.copy2(backdrop, backdrop_target / backdrop_name)

    film.poster.name = f"posters/{poster_name}"
    film.backdrop.name = f"backdrops/{backdrop_name}"

    film.save(update_fields=["poster", "backdrop"])

    print(f"Connected: {film.title}")

print("\nAll 40 films connected successfully!")
