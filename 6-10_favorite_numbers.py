# 6-10. Favorite Numbers: 

# Modify your program from Exercise 6-2 (page 102) so each person can have 
# more than one favorite number. 
# Then print each person’s name along with their favorite numbers.

favorite_numbers = {
	'nordine': [4,6,12,16],
	'albert': [3],
	'anthonin': [7,12,88],
	'hector': [12,1],
	'joachim': [45],
	}

for name, favorite_number_list in favorite_numbers.items():
	print("\n" + name.title() + "'s favorite numbers are:")
	for number in favorite_number_list:
		print("\t" + str(number))
