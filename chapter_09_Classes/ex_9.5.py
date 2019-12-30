class User:
	def __init__(self, first_name, last_name, username, email, login_attempts):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.email = email
		self.login_attempts = login_attempts

	def describe_user(self):
		print(f"Username: {self.username}")
		print(f"Email: {self.email}")
		print(f"Full name: {self.first_name} {self.last_name}")

	def greet_user(self):
		print(f"Hello, {self.first_name} !")

	def print_login_attempts(self):
		print(f"Number of login attempts for user {self.username}: {self.login_attempts}")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

user_0 = User('matthieu', 'boucard', 'mboucard', 'le.caribou@gmail.com', 12)

user_0.print_login_attempts()

for i in range(0,5):
	user_0.increment_login_attempts()
	user_0.print_login_attempts()

user_0.reset_login_attempts()
user_0.print_login_attempts()




