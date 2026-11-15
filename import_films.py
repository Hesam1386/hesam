
from django.utils.text import slugify
from movies.models import Film, Genre

films = [
    ("Dune", 2021, "Denis Villeneuve", ["Adventure", "Drama", "Fantasy"]),
    ("Batman: The Dark Knight", 2008, "Christopher Nolan", ["Action", "Crime", "Drama"]),
    ("Fight Club", 1999, "David Fincher", ["Drama", "Mystery"]),
    ("Mother!", 2017, "Darren Aronofsky", ["Drama", "Mystery"]),
    ("3-Iron", 2004, "Kim Ki-duk", ["Drama", "Romance", "Crime"]),
    ("The Lobster", 2015, "Yorgos Lanthimos", ["Drama", "Romance", "Science Fiction"]),
    ("Oldboy", 2003, "Park Chan-wook", ["Action", "Crime", "Mystery"]),
    ("Ex Machina", 2014, "Alex Garland", ["Drama", "Mystery", "Science Fiction"]),
    ("Shutter Island", 2010, "Martin Scorsese", ["Drama", "Mystery", "Crime"]),
    ("Leon: The Professional", 1994, "Luc Besson", ["Action", "Crime", "Drama"]),
    ("The Handmaiden", 2016, "Park Chan-wook", ["Drama", "Mystery", "Romance"]),
    ("Black Swan", 2010, "Darren Aronofsky", ["Drama", "Mystery"]),
    ("Upgrade", 2018, "Leigh Whannell", ["Action", "Crime", "Science Fiction"]),
    ("Parasite", 2019, "Bong Joon-ho", ["Drama", "Crime", "Mystery"]),
    ("Knives Out", 2019, "Rian Johnson", ["Crime", "Drama", "Mystery"]),
    ("Before Trilogy", 1995, "Richard Linklater", ["Drama", "Romance"]),
    ("Pulp Fiction", 1994, "Quentin Tarantino", ["Crime", "Drama"]),
    ("The Platform 1 & 2", 2019, "Galder Gaztelu-Urrutia", ["Drama", "Mystery", "Science Fiction"]),
    ("Inglourious Basterds", 2009, "Quentin Tarantino", ["Drama", "War", "Adventure"]),
    ("The Lord of the Rings", 2001, "Peter Jackson", ["Adventure", "Drama", "Fantasy"]),
    ("Mud", 2012, "Jeff Nichols", ["Adventure", "Drama", "Romance"]),
    ("Society of the Snow", 2023, "J. A. Bayona", ["Adventure", "Biography", "Drama"]),
    ("Don't Look Up", 2021, "Adam McKay", ["Drama", "Science Fiction"]),
    ("There Will Be Blood", 2007, "Paul Thomas Anderson", ["Drama", "Western"]),
    ("Pieces of a Woman", 2020, "Kornel Mundruczo", ["Drama"]),
    ("Memento", 2000, "Christopher Nolan", ["Drama", "Mystery", "Crime"]),
    ("Wild Tales", 2014, "Damian Szifron", ["Drama", "Crime"]),
    ("Bugonia", 2025, "Yorgos Lanthimos", ["Drama", "Science Fiction", "Mystery"]),
    ("Speak No Evil", 2024, "James Watkins", ["Drama", "Mystery"]),
    ("21 Grams", 2003, "Alejandro Gonzalez Inarritu", ["Drama", "Crime"]),
    ("Birdman", 2014, "Alejandro Gonzalez Inarritu", ["Drama", "Biography"]),
    ("The Shawshank Redemption", 1994, "Frank Darabont", ["Drama", "Crime"]),
    ("Amores Perros", 2000, "Alejandro Gonzalez Inarritu", ["Drama", "Crime"]),
    ("Her", 2013, "Spike Jonze", ["Drama", "Romance", "Science Fiction"]),
    ("Gone Girl", 2014, "David Fincher", ["Drama", "Mystery", "Crime"]),
    ("One Flew Over the Cuckoo's Nest", 1975, "Milos Forman", ["Drama"]),
    ("The Pursuit of Happyness", 2006, "Gabriele Muccino", ["Biography", "Drama"]),
    ("Memories of Murder", 2003, "Bong Joon-ho", ["Crime", "Drama", "Mystery"]),
    ("Room", 2015, "Lenny Abrahamson", ["Drama", "Mystery"]),
    ("Nuremberg", 2025, "James Vanderbilt", ["Biography", "Drama", "War"]),
]

created = 0
existing = 0

for title, year, director, genre_names in films:
    slug = slugify(title)

    film, was_created = Film.objects.get_or_create(
        slug=slug,
        defaults={
            "title": title,
            "year": year,
            "director": director,
        }
    )

    genres = Genre.objects.filter(name__in=genre_names)
    film.genres.set(genres)

    if was_created:
        created += 1
        print("Added:", title)
    else:
        existing += 1
        print("Updated genres:", title)

print(f"\nFinished! Added: {created} | Already existed: {existing}")
