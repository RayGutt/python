class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print("The restaurant named '" + self.restaurant_name.title() +
			"' serves " + self.cuisine_type + " food.")

	def open_restaurant(self):
		print("The restaurant '" + self.restaurant_name.title() + "' is open.")


restaurant_1 = Restaurant('La calabrese', 'italian')
restaurant_2 = Restaurant('tanakaki', 'japanese')
restaurant_3 = Restaurant('pierrot XIV', 'tradition')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
