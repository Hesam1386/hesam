from django.contrib import admin
from .models import Film, Genre, WatchItem


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "score", "review_status", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "director")
    filter_horizontal = ("genres",)

    @admin.display(boolean=True, description="نقد دارد")
    def review_status(self, obj):
        return obj.has_review


@admin.register(WatchItem)
class WatchItemAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "added_at")