def make_album(artist, title, track_number=0):
	"""Return a dictionary with the info provided"""
	album = {
		'artist': artist,
		'title': title,
		}
	if track_number:
		album['track_number'] = track_number
	return album

album = make_album('John McLaughlin', 'After The Rain')
print(album)

album = make_album('Slayer', 'Rain In Blood')
print(album)

album = make_album('A Tribe Called Quest', 'The Love Movement', track_number=12)
print(album)
