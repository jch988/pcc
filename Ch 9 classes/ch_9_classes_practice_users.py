


class User:
	
	user_list = []

	def __init__(self, first_name, last_name, username, password):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username
		self.password = password
		self.login_attempts = 0
		self.privileges_user = ['can add post', 'can remove own post']

		User.user_list.append(self.username)
		for name in User.user_list:
			if name in User.user_list in Admin.admin_list:
				User.user_list.pop()


	def describe_user(self):
		"""Prints a summary of the user's information"""
		print(f"\nThe user's first name is {self.first_name}, last name "
		f"is {self.last_name}, username is '{self.username}', and "
		f"password is '{self.password}'")

	def greet_user(self):
		"""Prints a personalized greeting to the user"""
		print(f"\tHello {self.username}!")

	def increment_login_attempts(self):
		"""Increments the login attempts by 1"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Resets the number of login attempts"""
		self.login_attempts = 0

	def show_privileges(self):
		"""Displays the privileges of a typical user"""
		print(f"{self.username} is a User. A user can:")
		for item in self.privileges_user:
			print(f"\t-{item}")



class Admin(User):
	"""A special type of User"""

	admin_list = []

	def __init__(self, first_name, last_name, username, password):
		"""Initialize the attributes from the parent class User"""
		super().__init__(first_name, last_name, username, password)
		"""Add attributes specific to Admin"""
		self.privileges = Privileges()
		Admin.admin_list.append(username)


class Privileges:

	def __init__(self):
		self.privileges_admin = ['can add user', 'can delete user', 
								'can add post', 'can delete post']

	def show_privileges(self):
		"""Displays the privileges"""
		print(f"This is an Admin account. The privileges are:")
		for item in self.privileges_admin:
			print(f"\t-{item}")



jholt88 = Admin('james', 'holt', 'jholt88', 'beetis')
wbrimley = User('wilford', 'brimely', 'wbrimley', 'checkyoursugar')
teddy = Admin('teddy', 'roosevelt', 'teddy', 'bigstick')
jdoe = User('john', 'doe', 'jdoe', 'doe')
hoe = User('hoe', 'bag', 'hohoho', 'imahoe')

print(f"User list: {User.user_list}")
print(f"Admin list: {Admin.admin_list}")

print(f"The admins are:")
for name in Admin.admin_list:
	print(name)

print()

print(f"The users are:")
for name in User.user_list:
	print(name)