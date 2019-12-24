def show_magicians(magicians):
	"""print the name of each magician in the parameter list"""
	for magician in magicians:
		print(magician.title())

def make_great(magicians):
	"""modify the list in the parameter list"""
	for magician in magicians:
		magicians(magician) = "The Great " + magicians(magician)

wizzards = [ 'malfoy', 'harry potter', 'merlin']

show_magicians(wizzards)

make_great(wizzards)

show_magicians(wizzards)
