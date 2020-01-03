reasons = []

while True:
	reason = input("Why do you like programming? ('q' to exit) ")
	if reason == 'q':
		break
	
	reasons.append(reason)

filename = 'data/programming_poll.txt'

#with open(filename, 'w') as file_object:
#	file_object.write(str(reasons))

with open(filename, 'a') as file_object:
	for reason in reasons:
		file_object.write(f"{reason}\n")
