class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print("The restaurant named '" + self.restaurant_name.title() +
			"' serves " + self.cuisine_type + " food.")

	def open_restaurant(self):
		print("The restaurant '" + self.restaurant_name.title() + "' is open.")


restaurant = Restaurant('La calabrese', 'italian')

print("The restaurant '" + restaurant.restaurant_name + "' serves " +
	restaurant.cuisine_type + " food.")

print("\nCalling describe_restaurant() method:")
restaurant.describe_restaurant()

print("\nCalling open_restaurant() method:")
restaurant.open_restaurant()

