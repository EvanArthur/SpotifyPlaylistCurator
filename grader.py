import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

tracks = []
index = 0

pop_total = 0

while True:
    results = sp.current_user_saved_tracks(limit=50, offset=index)
    count = 0
    for idx, item in enumerate(results["items"]):
        track = item["track"]
        # print(idx, track["artists"][0]["name"], " – ", track["name"])
        pop_total += track["popularity"]
        tracks.append(track["artists"][0]["name"] + " – " + track["name"])
        index += 1
        count += 1
    print(index)
    if count == 0:
        break

popularity = pop_total / len(tracks)
# for track in tracks:

#     print(track)

print("average Popularity:", popularity)
