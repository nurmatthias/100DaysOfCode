import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="xxxxxxxxxxxxxxxxxx",
                                               client_secret="xxxxxxxxxxxxxxxxxxxx",
                                               scope=scope,
                                               show_dialog=True,
                                               cache_path="day44/token.txt"))

user_id = sp.current_user()["id"]