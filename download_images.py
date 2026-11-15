from icrawler.builtin import BingImageCrawler
from pathlib import Path

movies = [
    "Dune 2021 movie poster",
    "The Dark Knight 2008 movie poster",
    "Fight Club 1999 movie poster",
    "Mother 2017 movie poster",
    "3-Iron 2004 movie poster",
    "The Lobster 2015 movie poster",
    "Oldboy 2003 movie poster",
    "Ex Machina 2014 movie poster",
    "Shutter Island 2010 movie poster",
    "Leon The Professional 1994 movie poster",
    "The Handmaiden 2016 movie poster",
    "Black Swan 2010 movie poster",
    "Upgrade 2018 movie poster",
    "Parasite 2019 movie poster",
    "Knives Out 2019 movie poster",
    "Before Trilogy movie poster",
    "Pulp Fiction 1994 movie poster",
    "The Platform 2019 movie poster",
    "Inglourious Basterds 2009 movie poster",
    "The Lord of the Rings movie poster",
    "Mud 2012 movie poster",
    "Society of the Snow 2023 movie poster",
    "Dont Look Up 2021 movie poster",
    "There Will Be Blood 2007 movie poster",
    "Pieces of a Woman 2020 movie poster",
    "Memento 2000 movie poster",
    "Wild Tales 2014 movie poster",
    "Bugonia 2025 movie poster",
    "Speak No Evil 2022 movie poster",
    "21 Grams 2003 movie poster",
    "Birdman 2014 movie poster",
    "The Shawshank Redemption 1994 movie poster",
    "Amores Perros 2000 movie poster",
    "Her 2013 movie poster",
    "Gone Girl 2014 movie poster",
    "One Flew Over the Cuckoos Nest 1975 movie poster",
    "The Pursuit of Happyness 2006 movie poster",
    "Memories of Murder 2003 movie poster",
    "Room 2015 movie poster",
    "Nuremberg movie poster",
]

poster_folder = Path(r"D:\posters")
poster_folder.mkdir(exist_ok=True)

for index, movie in enumerate(movies, start=1):
    print(f"Downloading {index}/40: {movie}")

    crawler = BingImageCrawler(
        storage={"root_dir": str(poster_folder / f"movie_{index:02d}")}
    )

    crawler.crawl(
        keyword=movie,
        max_num=1
    )

print("Finished!")