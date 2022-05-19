from new_section import new_section as ns

# 9-1 Restaurant

class Restaurant:

	def __init__(self, name, cuisine_type):
		self.name = name
		self.type = cuisine_type


	def describe_restaurant(self):
		"""Displays the name and type of food"""
		print(f"The name of the restaurant is {self.name}")
		print(f"The type of food at {self.name} is {self.type}")


	def open_restaurant(self):
		"""Indicates that the restaurant is open"""
		print(f"Want {self.type}? {self.name} is open!")


my_restaurant = Restaurant('The Ho Cafe', 'Indian')

print(f"My restaurant's name is {my_restaurant.name}")
print(f"My restaurant serves {my_restaurant.type} food")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

ns()

# 9-2 Three restaurants

wilfords_restaurant = Restaurant('Super Diabetes', 'Maple syrup')
breakfast_restaurant = Restaurant('The AM Outlet', 'Breakfast')
taco_restaurant = Restaurant('Taco-Taco-Taco', 'Tacos')

wilfords_restaurant.describe_restaurant()
wilfords_restaurant.open_restaurant()
print()
breakfast_restaurant.describe_restaurant()
breakfast_restaurant.open_restaurant()
print()
taco_restaurant.describe_restaurant()
taco_restaurant.open_restaurant()

ns()

# 9-3 Users

class User:
	
	user_number = 0
	user_list = []
	removed_list = []
	user_num_dict = {}

	def __init__(self, first_name, last_name, username, password):
		
		if username not in User.user_list:

			self.first_name = first_name.title()
			self.last_name = last_name.title()
			self.username = username
			self.password = password

			User.user_number += 1
			self.user_number = User.user_number

			User.user_list.append(self.username)
			User.user_num_dict[self.user_number] = self.username

		elif username in User.user_list:
			print(f"\nSorry, the username '{username}' is already taken. "
				f"Please pick a different one.")

	def describe_user(self):
		"""Prints a summary of the user's information"""
		print(f"\nUser number {self.user_number}! First name is {self.first_name}, last name "
		f"is {self.last_name}, username is '{self.username}', and "
		f"password is '{self.password}'")
		User.greet_user(self)
		User.list_users()

	def greet_user(self):
		"""Prints a personalized greeting to the user"""
		print(f"Hello {self.username}! You are user number {self.user_number}.")

	def list_users():
		if User.user_list:
			print("The current users are:")
			for user in User.user_list:
				print(f"\t{user}")

		if User.removed_list:
			print("The removed users are:")
			for user in User.removed_list:
				print(f"\t{user}")
		else:
			print("There are currently no users")

	def list_users_by_number():
		for number, username in User.user_num_dict.items():
			print(f"{number}. {username}")

	def remove_user(self):
		"""Removes a user from the User List and puts them on the Removed User List"""
		"""They still are an instance and appear in the user num dictionary"""
		User.user_list.remove(self.username)
		User.removed_list.append(self.username)
		print(f"{self} has been removed")
		User.list_users()

	def recover_password(self):
		print(f"The password for {self.username} is '{self.password}'")

	def get_user_number(self):
		print(f"The user number for {self.username} is {self.user_number}")

	def __str__(self):
		return f"{self.first_name} {self.last_name}"


User.list_users()

jholt = User('james', 'holt', 'jholt88', 'beetis')
jholt.describe_user()

rogan = User('joe', 'rogan', 'greatandpowerful', 'haveyoutrieddmt?')
rogan.describe_user()

wbrimley = User('wilford', 'brimely', 'wbrimley', 'checkyoursugar')
wbrimley.describe_user()

teddy = User('teddy', 'roosevelt', 'teddy','bigstick')
teddy.describe_user()

putin = User('vladimir', 'putin', 'greatandpowerful', 'russia4ever')
putin = User('vladimir', 'putin', 'greaterandpowerfuler', 'russia4ever')
putin.describe_user()


putin.remove_user()

jholt.recover_password()
jholt.password = 'diabeetis'
jholt.recover_password()
wbrimley.get_user_number()

obama = User('barack', 'obama', 'prez44', 'change')
obama.describe_user()

ns()

User.list_users_by_number()