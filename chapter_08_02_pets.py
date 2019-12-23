def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""

	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

print("\nWrong arguments order in the call to function describe_pet()")
describe_pet('harry', 'hamster')