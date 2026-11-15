
from icrawler.builtin import BingImageCrawler
from pathlib import Path

movies = [
    "Dune 2021 film landscape backdrop",
    "The Dark Knight 2008 film backdrop",
    "Fight Club 1999 film backdrop",
    "Mother 2017 film backdrop",
    "3-Iron 2004 film backdrop",
    "The Lobster 2015 film backdrop",
    "Oldboy 2003 film backdrop",
    "Ex Machina 2014 film backdrop",
    "Shutter Island 2010 film backdrop",
    "Leon The Professional 1994 film backdrop",
    "The Handmaiden 2016 film backdrop",
    "Black Swan 2010 film backdrop",
    "Upgrade 2018 film backdrop",
    "Parasite 2019 film backdrop",
    "Knives Out 2019 film backdrop",
    "Before Trilogy film backdrop",
    "Pulp Fiction 1994 film backdrop",
    "The Platform 2019 film backdrop",
    "Inglourious Basterds 2009 film backdrop",
    "The Lord of the Rings film backdrop",
    "Mud 2012 film backdrop",
    "Society of the Snow 2023 film backdrop",
    "Don't Look Up 2021 film backdrop",
    "There Will Be Blood 2007 film backdrop",
    "Pieces of a Woman 2020 film backdrop",
    "Memento 2000 film backdrop",
    "Wild Tales 2014 film backdrop",
    "Bugonia 2025 film backdrop",
    "Speak No Evil 2022 film backdrop",
    "21 Grams 2003 film backdrop",
    "Birdman 2014 film backdrop",
    "The Shawshank Redemption 1994 film backdrop",
    "Amores Perros 2000 film backdrop",
    "Her 2013 film backdrop",
    "Gone Girl 2014 film backdrop",
    "One Flew Over the Cuckoo's Nest 1975 film backdrop",
    "The Pursuit of Happyness 2006 film backdrop",
    "Memories of Murder 2003 film backdrop",
    "Room 2015 film backdrop",
    "Nuremberg film backdrop",
]

folder = Path(r"D:\photo site")
folder.mkdir(parents=True, exist_ok=True)

for index, movie in enumerate(movies, start=1):
    print(f"Downloading {index}/40: {movie}")

    crawler = BingImageCrawler(
        storage={"root_dir": str(folder / f"movie_{index:02d}")}
    )
    crawler.crawl(keyword=movie, max_num=1)

print("Finished!")
