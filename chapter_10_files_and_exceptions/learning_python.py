filename = 'data/learning_python.txt'

print("1. Printing by reading in the entire file:\n")
with open(filename) as file_object:
	contents = file_object.read()
print(contents)

print("\n2. Printing by lopping over the file object:\n")
with open(filename) as file_object_2:
	for line in file_object_2:
		print(line)

print("\n3. Printing lines in a list:\n")
with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line)
