from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("reviews/", views.reviews, name="reviews"),
    path("watched/", views.watched, name="watched"),
    path("unwatched/", views.unwatched, name="unwatched"),
    path("genre/<str:slug>/", views.genre_films, name="genre"),
    path("film/<str:slug>/", views.film_detail, name="film_detail"),
]