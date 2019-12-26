class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("The restaurant named '" + self.restaurant_name.title() +
			"' serves " + self.cuisine_type + " food.")

	def open_restaurant(self):
		print("The restaurant '" + self.restaurant_name.title() + "' is open.")

	def set_number_served(self, number):
		self.number_served = number	

	def increment_number_served(self, number):
		self.number_served += number

restaurant = Restaurant('La calabrese', 'italian')

print("The restaurant '" + restaurant.restaurant_name + "' serves " +
	restaurant.cuisine_type + " food.")

print("\nCalling describe_restaurant() method:")
restaurant.describe_restaurant()

print("\nCalling open_restaurant() method:")
restaurant.open_restaurant()

print("\nNumber of customers served: ")
print(restaurant.number_served)

print("\nChanging the number of customers served directly.")
restaurant.number_served = 5

print("\nNumber of customers served: ")
print(restaurant.number_served)

print("\nChanging the number of customers served with set_number_served().")
restaurant.set_number_served(12)

print("\nNumber of customers served: ")
print(restaurant.number_served)

print("\nChanging the number of customers served with increment_number_served().")
restaurant.increment_number_served(3)

print("\nNumber of customers served: ")
print(restaurant.number_served)

