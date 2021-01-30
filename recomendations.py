import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

results = sp.recommendations(seed_genres=["house"])
for i in results["tracks"]:
    print(i["artists"][0]["name"])
    print(i["name"])