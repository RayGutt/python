from user import User
from admin import Privileges, Admin

my_admin = Admin('matthieu', 'boucard', 'mboucard', 'mbouc@doman', 2)
my_admin.privileges.privileges = [
	'can fuck everything',
	'can delete user', 
	'can ban user',
	]

my_admin.privileges.show_privileges()
