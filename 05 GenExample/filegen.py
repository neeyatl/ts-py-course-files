import os

root = 'music'

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        for f in files:
            song_deets = f[:-5].split(" - ")
            print(song_deets)
        input()
