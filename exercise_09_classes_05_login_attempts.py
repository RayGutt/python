class User():
	def __init__(self, first_name, last_name, username, email, age):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.email = email
		self.age = age
		self.login_attempts = 0

	def describe_user(self):
		"""Describe user"""
		print("The user " + self.username + " name is " +
			self.first_name.title() + " " + self.last_name.title() +
			", his/her email is " + self.email + " and he/she is " +
			str(self.age) + " years old.")

	def greet_user(self):
		"""Greet user"""
		print("Hello " + self.first_name.title() + " " + self.last_name.title())

	def increment_login_attempts(self):
		"""Increment the number of login attempts"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Reset the number of login attempts"""
		self.login_attempts = 0

user_1 = User('Matthieu', 'Boucard', 'mboucard', 'le.caribou@gmail.com', 46)
user_2 = User('René', 'Descamps', 'rdescamps', 'rene@hotmail.com', 66)
user_3 = User('Zinédine', 'Zidane', 'zizou', 'zizou@fff.fr', 44)

user_1.describe_user()
user_1.greet_user()


user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

user_1.increment_login_attempts()
print(f"Number of login attempts for {user_1.username}: {user_1.login_attempts}.")

user_1.reset_login_attempts()
print(f"Number of login attempts for {user_1.username}: {user_1.login_attempts}.")
