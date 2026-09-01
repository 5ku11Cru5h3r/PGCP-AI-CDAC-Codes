playlist=["Inception", "The Matrix", "Interstellar"]
movie_name=input()
if movie_name in playlist:
    print("Already added")
else:
    playlist.append(movie_name)
print(sorted(playlist))