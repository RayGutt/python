# 6-8. Pets: 

# Make several dictionaries, where the name of each dictionary is the name of a pet. 
# In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. 
# Next, loop through your list and as you do print everything you know about each pet.

pets = []

pet = {
	'name': 'medor', 
	'kind': 'dog',
	'owner': 'raymond',
	}

pets.append(pet)

pet = {
	'name': 'minou',
	'kind': 'cat',
	'owner': 'ginette',
	}

pets.append(pet)

pet = {
	'name': 'bugs',
	'kind': 'rabbit',
	'owner': 'alphonse',
	}

pets.append(pet)

for pet in pets:
	print(pet['name'] + " is a " + 
		pet['kind'] + " and its owner is " + 
		pet['owner'])
