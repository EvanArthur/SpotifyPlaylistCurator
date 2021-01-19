import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.user_playlists("spotify")

count = 0

with open("tracks1.csv", mode="w") as track_file:
    csv_writer = csv.writer(
        track_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    csv_writer.writerow(
        [
            "id",
            "song_name",
            "song_artist",
            "danceability",
            "energy",
            "key",
            "loudness",
            "mode",
            "speechiness",
            "acousticness",
            "instrumentalness",
            "liveness",
            "valence",
            "tempo",
            "type",
            "id",
            "uri",
            "track_href",
            "analysis_url",
            "duration_ms",
            "time_signature",
        ]
    )
    while playlists:
        for i, playlist in enumerate(playlists["items"]):
            print(
                "%4d %s %s"
                % (i + 1 + playlists["offset"], playlist["uri"], playlist["name"])
            )
            try:
                result = sp.playlist_items(playlist["id"])
            except:
                continue

            for song in result["items"]:
                try:
                    if song["track"] != None:
                        # print(song["track"].keys())
                        metrics = sp.audio_features(tracks=[song["track"]["id"]])
                        if metrics[0] != None:
                            # print(metrics[0].keys())
                            song_id = song["track"]["id"]
                            song_name = song["track"]["name"]
                            song_artist = song["track"]["artists"][0]["name"]
                            entry = list(metrics[0].values())
                            entry = [song_id, song_name, song_artist] + entry
                            csv_writer.writerow(entry)
                            if count % 100 == 0:
                                print(count)
                            count += 1
                            # print(entry)
                except:
                    continue

        if playlists["next"]:
            playlists = sp.next(playlists)
        else:
            playlists = None