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


class Privileges:
	def __init__(self, privileges=[]):
		self.privileges = privileges

	def show_privileges(self):
		if self.privileges:
			print("Privileges: ")
			for privilege in self.privileges:
				print(f"\t- {privilege}")
		else:
			print("User has no privileges.")


class Admin(User):
	def __init__(self, first_name, last_name, username, email, login_attempts):
		super().__init__(first_name, last_name, username, email, login_attempts)
		self.privileges = Privileges()


my_admin = Admin('matthieu', 'boucard', 'mboucard', 'matbouc@domain', 0)
my_admin.describe_user()
my_admin.privileges.show_privileges()

my_admin.privileges.privileges = [
	'can ban user', 
	'can delete account', 
	'can add post'
	]
my_admin.privileges.show_privileges()
