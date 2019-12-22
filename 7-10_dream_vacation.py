# 7-10. Dream Vacation: 
# Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.

vacation_poll = {}

while True:
	name = input("\nWhat's your name? (type 'quit' to exit poll) ")
	if name == 'quit':
		break
	place = input("\nIf you could visit one place in the world, where would you go ?")

	vacation_poll[name] = place

# results

print("\n\nResults of the poll: ")
for name, place in vacation_poll.items():
	print(name.title() + " wants to go to " + place.title())


