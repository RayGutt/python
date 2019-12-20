current_users = ['mboucard', 'admin', 'john', 'zobi', 'luka' ]

new_users = ['Mboucard', 'hector', 'zobi', 'bibovski', 'leila']

for user in new_users:
	if user.lower() in current_users:
		print("username " + user + " already in use, pick another username")
	else:
		print("username " + user + " available")

