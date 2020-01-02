from random import choice

items = [ 10, 14, 22, 36, 121, 200, 285, 305, 535, 900, 'A', 'G', 'I', 'M', 'Z']

select = ''

for i in range(0,4):
	select += str(choice(items)) + " "

print(f"The lottery result is: {select}")
