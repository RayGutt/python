def show_magicians(magicians):
	"""print the name of each magician in the parameter list"""
	for magician in magicians:
		print(magician.title())

wizzards = [ 'malfoy', 'harry potter', 'merlin']

show_magicians(wizzards)
