from django.db.models import F
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, render
from .models import Film, Genre, WatchItem


def ranked_films():
    # فقط فیلم‌های نمره‌دار، از بالاترین نمره
    return Film.objects.filter(score__isnull=False).order_by("-score")


def reviewed_films():
    # فقط فیلم‌های نقددار، جدیدترین نقد اول
    return Film.objects.exclude(review="").order_by(
        F("reviewed_at").desc(nulls_last=True), "-created_at"
    )


def attach_ranks(films):
    # رتبه‌ی واقعی هر فیلم تو جدول رو کنارش می‌ذاره (برای فیلم بدون نمره None)
    rank_map = {f.pk: i for i, f in enumerate(ranked_films(), start=1)}
    films = list(films)
    for f in films:
        f.table_rank = rank_map.get(f.pk)
    return films


def home(request):
    q = request.GET.get("q", "").strip()
    context = {"q": q}

    if q:
        context["films"] = attach_ranks(Film.objects.filter(title__icontains=q))
    else:
        latest = list(reviewed_films()[:4])
        context["films"] = attach_ranks(ranked_films())
        context["latest"] = latest
        context["hero"] = latest[0] if latest else None

    return render(request, "film/home.html", context)


def reviews(request):
    return render(request, "film/reviews.html", {"films": reviewed_films()})


def watched(request):
    films = Film.objects.order_by(Lower("title"))
    return render(request, "film/watched.html", {"films": films})


def unwatched(request):
    return render(request, "film/unwatched.html", {"items": WatchItem.objects.all()})


def genre_films(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    films = genre.films.filter(score__isnull=False).order_by("-score")
    return render(request, "film/genre.html", {
        "genre": genre,
        "films": attach_ranks(films),
    })


def film_detail(request, slug):
    film = get_object_or_404(Film, slug=slug)
    return render(request, "film/film_detail.html", {"film": film})