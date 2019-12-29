class Restaurant:
	def	__init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"This restaurant is called {self.restaurant_name} and serves {self.cuisine_type} food.")

	def open_restaurant(self):
		print(f"The restaurant {self.restaurant_name} is open.")

restaurant_1 = Restaurant('La Calabrese', 'Italian')
restaurant_2 = Restaurant('Nguyen', 'vietnamese')
restaurant_3 = Restaurant('Au XIV juillet', 'french')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
