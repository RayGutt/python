usernames = ['mboucard', 'admin', 'toto', 'titi', 'tutu', 'zobi']

for username in usernames:
	if username == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print("Hello " + username + ", thank for logging in again.")
