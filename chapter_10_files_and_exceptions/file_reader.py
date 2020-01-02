file_path='/home/matthieu/Matthieu/repos/python/chapter_10_files_and_exceptions/data/pi_digits.txt'
with open(file_path) as file_object:
	contents = file_object.read()
print(contents.rstrip())
