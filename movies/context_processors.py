from .models import Genre


def sidebar(request):
    return {"sidebar_genres": Genre.objects.all()}