class Restaurant:
	def	__init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"This restaurant is called {self.restaurant_name} and serves {self.cuisine_type} food.")

	def open_restaurant(self):
		print(f"The restaurant {self.restaurant_name} is open.")

	def set_number_served(self, number):
		self.number_served = number 

	def increment_number_served(self, number):
		self.number_served += number