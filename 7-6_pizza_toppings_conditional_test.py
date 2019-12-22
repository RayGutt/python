# 7-4. Pizza Toppings: 
# Write a loop that prompts the user to enter a series of pizza toppings 
# until they enter a 'quit' value. 
# As they enter each topping, print a message saying 
# you’ll add that topping to their pizza.

message = "\nWhat topping do you want to add to your pizza?"
message += "\nType 'quit' when you're done. "

topping = ''

while topping != 'quit':
	topping = input(message)
	if topping != 'quit':
		print("We'll add a " + topping + " topping to your pizza")
