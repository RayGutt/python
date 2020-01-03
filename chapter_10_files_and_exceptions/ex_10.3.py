name = input("What is your name? ")

filename = 'data/guest.txt'
with open(filename, 'w') as object_file:
	object_file.write(name)
