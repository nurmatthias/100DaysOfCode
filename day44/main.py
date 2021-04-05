from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


BILL_BOARD_URL = "https://www.billboard.com/charts/hot-100/"

date = input("To which date you want to travel back? (YYYY-MM-DD): ")

response = requests.get(BILL_BOARD_URL+date)
response.raise_for_status()


soup = BeautifulSoup(response.text, "html.parser")


song_list = [song.getText() for song in soup.find_all(name="span", class_="chart-element__information__song")]
song_artist_list = [artist.getText() for artist in soup.find_all(name="span", class_="chart-element__information__artist")]


scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="xxxxxxxxxxxxxxx",
                                               client_secret="xxxxxxxxxxxxxx",
                                               scope=scope,
                                               show_dialog=True,
                                               cache_path="day44/token.txt"))

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)