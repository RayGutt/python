def print_ingredients(ingredients):
	"""print the list of ingredients provided by the parameter"""
	print("\nHere's what's in your sandwich: ")
	for ingredient in ingredients:
		print(" - " + ingredient)

ingredients_list = ['salad', 'tomato', 'cheese']

print_ingredients(ingredients_list)

print_ingredients(['tuna', 'tomato'])
