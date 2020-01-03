filename = 'data/guest_book.txt'

while True:
	name = input("What is your name? ('q' to exit) ")
	if name == 'q':
		break
	
	with open(filename, 'a') as file_object:
		line = name + "\n"
		file_object.write(line)

	print(f"Hello, {name}")
