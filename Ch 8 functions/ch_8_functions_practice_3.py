# 8-6 City names

def city_country(city, country, state =""):
	"""Return the name of a city and country"""
	if state:
		answer = f"{city}, {state}, {country}"
	else:
		answer = f"{city}, {country}"
	return answer.title()

location = city_country('san antonio', 'united states', 'texas')
print(location)

location = city_country('lima', 'peru')
print(location)

location = city_country('moscow', 'russia')
print(location)

location = city_country('vancouver', 'canada', 'british columbia')
print(location)


print()

# 8-7 Album

def make_album(artist_name, album_title, songs=None):
	"""Build a dictionary describing a music ablum"""
	if songs:
		album_dictionary = {"artist": artist_name, "title": album_title, 'songs': songs,}
	else:
		album_dictionary = {"artist": artist_name, "title": album_title,}
	return album_dictionary

album = make_album('rush', 'moving pictures', 7)
print(album)
album = make_album('marvin gaye', "what's going on")
print(album)
album = make_album('van halen', '1984', 9)
print(album)


print()

# 8-8 User Album

album_collection = {}

while True:
	print("Give me an artist and album title. I'll add it to the list."
		" Enter 'q' to stop adding")
	artist = input("Artist: ")
	if artist == 'q':
		break
	album = input("Album: ")
	if album == 'q':
		break

	addition = make_album(artist.title(), album.title())
	print(f"\nHere is the current addition:\n\t{addition}\n")


# I want to modify this to add each addition to a comprehensive dictionary,
# and print it out each time

	album_collection[artist.title()] = album.title()

	print(f"Here is the current collection (artist: album): \n\t {album_collection}\n")

# AND THAT'S HOW IT'S DONE!!!

# is there a way to print it out in a more readable format?

	for artist, album in album_collection.items():
		print(f"\tartist: {artist.title()} \n\t album: {album.title()}\n")

# YASSSS THIS IS IT!!!!!!!!11!!11!!!!!
# the only real issue is that this doesn't use the 'make_album' function at all
# COME BACK TO THIS LATER

# this seems to do it:

def album_input():
	"""Allow user to add new entries to the 'albums' dictionary"""
	albums = {}
	print("Tell me an artist and album, and I'll add it. Enter 'q' to stop")
	while True:
		artist = input("Artist ")
		if artist == 'q':
			break
		album = input("Album: ")
		if album == 'q':
			break
		else:
			albums[artist] = album
			print(f"Adding selection. The current list is:")
			for artist, album in albums.items():
				print(f"\t{artist.title()}: {album.title()}")
			print()

album_input()

# now I want to be able to take the 'albums' dictionary out and use is elsewhere
# want to run another function where I print the final album collection

