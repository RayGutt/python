from random import choice


def get_select():
	select = ''
	for i in range(0,4):
		select += str(choice(items)) + " "

	select = select.rstrip()
	return(select)
	

items = [ 10, 14, 22, 36, 121, 200, 285, 305, 535, 900, 'A', 'G', 'I', 'M', 'Z']
my_ticket='10 A G 36'

iteration = 0

while True:
	my_select = get_select()
	if my_select == my_ticket:
		print(f"Success, after {iteration} iterations")
		break
	else:
		iteration += 1
		print(f"{iteration}: \t{my_select}")

