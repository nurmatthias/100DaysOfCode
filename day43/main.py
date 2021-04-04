from bs4 import BeautifulSoup
import requests


URL = "https://www.filmempfehlung.com/die-top-100.html"

response = requests.get(URL)
response.raise_for_status()


soup = BeautifulSoup(response.text, "html.parser")

movie_rankings = [int(ranking.getText()) for ranking in soup.find_all(name="span", class_="platznr round")]
movies = [movie.getText().split("OT:") for movie in soup.find_all(name="p", class_="ottitel tc")]

for index, rank in enumerate(movie_rankings):
    print(f"{rank}: {movies[index][0]} {'(OT:' + movies[index][1] + ')' if 1 < len(movies[index]) else ''}")
