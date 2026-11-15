from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField("ژانر", max_length=50)
    slug = models.SlugField("آدرس", unique=True, allow_unicode=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField("نام فیلم", max_length=200)
    slug = models.SlugField("آدرس صفحه", unique=True, allow_unicode=True)
    year = models.PositiveIntegerField("سال ساخت")
    director = models.CharField("کارگردان", max_length=150, blank=True)
    poster = models.ImageField("پوستر", upload_to="posters/")
    backdrop = models.ImageField("تصویر افقی بنر (اختیاری)", upload_to="backdrops/", blank=True)
    score = models.DecimalField(
        "نمره از ۱۰۰", max_digits=5, decimal_places=2, null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="خالی بذاری، فیلم تو جدول رتبه‌بندی نمیاد",
    )
    genres = models.ManyToManyField(Genre, verbose_name="ژانرها", blank=True, related_name="films")
    review = models.TextField("نقد", blank=True, help_text="اختیاریه")
    synopsis = models.TextField(
    "خلاصه داستان",
    max_length=500,
    blank=True)
    watched_on = models.DateField("تاریخ تماشا", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True, editable=False)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} ({self.year})"

    @property
    def has_review(self):
        return bool(self.review.strip())

    @property
    def rank(self):
        # رتبه‌ی فیلم تو جدول؛ برای فیلم بدون نمره None برمی‌گردونه
        if self.score is None:
            return None
        return Film.objects.filter(score__gt=self.score).count() + 1

    def save(self, *args, **kwargs):
        # اولین باری که نقد نوشته می‌شه، زمانش ثبت می‌شه
        if self.has_review and self.reviewed_at is None:
            self.reviewed_at = timezone.now()
        super().save(*args, **kwargs)


class WatchItem(models.Model):
    title = models.CharField("نام فیلم", max_length=200)
    year = models.PositiveIntegerField("سال ساخت", null=True, blank=True)
    poster = models.ImageField("پوستر (اختیاری)", upload_to="watchlist/", blank=True)
    note = models.CharField("یادداشت کوتاه", max_length=200, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-added_at"]

    def __str__(self):
        return self.title


