from user import User

class Admin(User):
	"""A special type of User"""

	def __init__(self, first_name, last_name, username, password):
		"""Initialize the attributes from the parent class User"""
		super().__init__(first_name, last_name, username, password)
		"""Add attributes specific to Admin"""
		self.privileges = Privileges()


class Privileges:

	def __init__(self):
		self.privileges_admin = ['can add user', 'can delete user', 
								'can add post', 'can delete post']
	def show_privileges(self):
		"""Displays the privileges"""
		print(f"This is an Admin account. The privileges are:")
		for item in self.privileges_admin:
			print(f"\t-{item}")

