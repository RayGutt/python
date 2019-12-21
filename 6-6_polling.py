favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

should_take_the_poll = [
	'norbert',
	'zinedine',
	'sarah',
	'phil',
	'hector',
	]

for people in should_take_the_poll:
	print("\n" + people.title())

	if people in favorite_languages.keys():
		print("\tThank you for responding!")
	else:
		print("\tYou should take the poll...")
