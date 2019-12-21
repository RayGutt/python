person_0 = {
	'first_name': 'norbert',
	'last_name': 'rotrou',
	'age': 41,
	'city': 'brie-comte-robert',
	}
person_1 = {
	'first_name': 'jean',
	'last_name': 'ducon',
	'age': 40,
	'city': 'trifouilli',
	}
person_2 = {
	'first_name': 'albert',
	'last_name': 'zobi',
	'age': 23,
	'city': 'maroilles',
	}


people = [person_0, person_1, person_2]


for person in people:
	print("Name: " + person['first_name'].title() +
		" " + person['last_name'].title() + ".")

	print("Age: " + str(person['age']))

	print("City: " + person['city'].title())

