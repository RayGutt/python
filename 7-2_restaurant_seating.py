# 7-2. Restaurant Seating: 
# Write a program that asks the user how many people are in their dinner group. 
# If the answer is more than eight, print a message saying they’ll have to wait 
# for a table. Otherwise, report that their table is ready.

message = "How many people are in your dinner group? "

answer = input(message)

answer = int(answer)

if answer > 8:
	print("You'll have to wait for a table.")
else:
	print("Your table is ready.")
