from more_itertools import unique_everseen

with open("tracks1.csv", "r") as f, open("tracks_unique.csv", "w") as out_file:
    out_file.writelines(unique_everseen(f))