def make_album(artist, title, track_number=0):
	"""Return a dictionary with the info provided"""
	album = {
		'artist': artist,
		'title': title,
		}
	if track_number:
		album['track_number'] = track_number
	return album

while True:
	print("Please enter album info")
	print("(Type 'q' to exit at any time)")
	artist = input("Artist: ")
	if artist == 'q':
		break

	title = input("Album's title: ")
	if title == 'q':
		break

	track_number = input("Number of tracks (can be NULL): ")
	if track_number == 'q':
		break

	album = make_album(artist, title, track_number)
	print(album)
