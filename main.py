import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.user_playlists("spotify")


while playlists:
    for i, playlist in enumerate(playlists["items"]):
        print(
            "%4d %s %s"
            % (i + 1 + playlists["offset"], playlist["uri"], playlist["name"])
        )
        result = sp.playlist_items(playlist["id"])
        for song in result["items"]:
            if song["track"] != None:
                # print(song["track"].keys())
                metrics = sp.audio_features(tracks=[song["track"]["id"]])
                print(metrics[0].keys())
                # print(song["track"]["id"])
                # print(song["track"]["name"])

    if playlists["next"]:
        playlists = sp.next(playlists)
    else:
        playlists = None