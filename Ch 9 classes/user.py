class User:
	
	def __init__(self, first_name, last_name, username, password):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.password = password
		self.login_attempts = 0
		self.privileges_user = ['can add post', 'can remove own post']

	def describe_user(self):
		"""Prints a summary of the user's information"""
		print(f"\nThe user's first name is {self.first_name.title()}, last name "
		f"is {self.last_name.title()}, username is '{self.username}', and "
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
