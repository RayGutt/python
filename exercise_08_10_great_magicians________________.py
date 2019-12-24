def show_magicians(magicians):
	"""print the name of each magician in the parameter list"""
	for magician in magicians:
		print(magician.title())

def make_great(magicians):
	"""modify the list in the parameter list"""

	# start with an empty list
	great_magicians = []

	for magician in magicians:
		great_magicians.append(magician + "The Great ")

	magicians = []

	for magician in great_magicians:
		magicians.append(magician)


magicians = [ 'malfoy', 'harry potter', 'merlin']

print("List before calling the function")
show_magicians(magicians)


print("\nList after calling the function")
make_great(magicians)

show_magicians(magicians)
