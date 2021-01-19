from scipy.spatial import distance
import csv

# danceability,energy,speechiness,acousticness,valence
target = [0.773, 0.414, 0.0961, 0.00411, 0.289]

# target = [0.62, 0.936, 0.0308, 0.0261, 0.763]

# target = [0.537, 0.819, 0.0866, 0.061, 0.832]

songs = []

with open("tracks_unique.csv", newline="", mode="r") as csvfile:
    reader = csv.DictReader(csvfile)
    count = 0
    for row in reader:

        song = [
            float(row["danceability"]),
            float(row["energy"]),
            float(row["speechiness"]),
            float(row["acousticness"]),
            float(row["valence"]),
        ]

        dist = distance.euclidean(target, song)
        if len(songs) <= 20:
            songs.append([row["song_name"], row["song_artist"], dist])
            sorted(songs, key=lambda x: x[2])
        else:
            if dist < songs[-1][2]:
                songs.remove(songs[-1])
                songs.append([row["song_name"], row["song_artist"], dist])
                songs.sort(key=lambda x: x[2])
                # print(songs)
        if count % 100 == 0:
            print(count)
        count += 1


print(songs)
# print(row["song_name"], row["song_artist"])
# id,song_name,song_artist,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,type,id,uri,track_href,analysis_url,duration_ms,time_signature

# "Hold On, We're Going Home",Drake,0.773,0.414,6,-7.436,0,0.0961,0.00411,3.4e-05,0.0733,0.289,99.993,audio_features,6jdOi5U5LBzQrc4c1VT983,spotify:track:6jdOi5U5LBzQrc4c1VT983,https://api.spotify.com/v1/tracks/6jdOi5U5LBzQrc4c1VT983,https://api.spotify.com/v1/audio-analysis/6jdOi5U5LBzQrc4c1VT983,227880,4
# You Can't Hurry Love - 2016 Remaster,Phil Collins,0.62,0.936,7,-4.593,1,0.0308,0.0261,0,0.0679,0.763,97.527,audio_features,4YwbSZaYeYja8Umyt222Qf,spotify:track:4YwbSZaYeYja8Umyt222Qf,https://api.spotify.com/v1/tracks/4YwbSZaYeYja8Umyt222Qf,https://api.spotify.com/v1/audio-analysis/4YwbSZaYeYja8Umyt222Qf
# [0.62,0.936,0.0308,0.0261,0.763]
# print(distance.euclidean([1, 0, 0, 3], [0, 1, 0, 3]))

# 0MgOsVty0YR1kas7x16yoS,Freaking Out The Neighborhood,Mac DeMarco,0.573,0.819,8,-5.735,0,0.0866,0.061,0.029,0.386,0.832,143.263,audio_features,0MgOsVty0YR1kas7x16yoS,spotify:track:0MgOsVty0YR1kas7x16yoS,https://api.spotify.com/v1/tracks/0MgOsVty0YR1kas7x16yoS,https://api.spotify.com/v1/audio-analysis/0MgOsVty0YR1kas7x16yoS,173867,4
