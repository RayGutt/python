from user import User

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
