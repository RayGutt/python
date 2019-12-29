class Restaurant:
	def	__init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"This restaurant is called {self.restaurant_name} and serves {self.cuisine_type} food.")

	def open_restaurant(self):
		print(f"The restaurant {self.restaurant_name} is open.")


restaurant = Restaurant('La calabrese', 'italian')

print(f"Name: {restaurant.restaurant_name}")
print(f"Food type: {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()
