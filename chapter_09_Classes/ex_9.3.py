class User:
	def __init__(self, first_name, last_name, username, email):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.email = email

	def describe_user(self):
		print(f"Username: {self.username}")
		print(f"Email: {self.email}")
		print(f"Full name: {self.first_name} {self.last_name}")

	def greet_user(self):
		print(f"Hello, {self.first_name} !")

user_0 = User('matthieu', 'boucard', 'mboucard', 'le.caribou@gmail.com')
user_1 = User('norbert', 'zobi', 'nzobi', 'norbert@hotmail')
user_2 = User('Zoé', 'zimoula', 'zz', 'zozi@gmail.com')

user_0.describe_user()
user_0.greet_user()


user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

