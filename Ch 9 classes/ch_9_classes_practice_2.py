from new_section import new_section as ns

# 9-4 Number served


class Restaurant():

	def __init__(self, name, cuisine_type):
		self.name = name.title()
		self.type = cuisine_type
		self.number_served = 0


	def describe_restaurant(self):
		"""Displays the name and type of food"""
		print(f"The name of the restaurant is {self.name}")
		print(f"The type of food at {self.name} is {self.type}")
		print(f"So far {self.name} has served {self.number_served} customers")

	def open_restaurant(self):
		"""Indicates that the restaurant is open"""
		print(f"Want {self.type}? {self.name} is open!")

	def number_served(self, served):
		"""Show how many customers have been served"""
		number_served = served

	def show_number_served(self):
		"""Print out how many customers have been served so far"""
		print(f"{self.name} has served {self.number_served} customers!")

	def set_number_served(self, customers):
		"""Set the number of customers that have been served"""
		self.number_served = customers

	def increment_number_served(self, customers):
		"""Increment the number of customers served"""
		self.number_served += customers



wb = Restaurant('whataburger', 'burgers')
sal = Restaurant('salata', 'salads')

wb.describe_restaurant()
sal.describe_restaurant()

wb.open_restaurant()
sal.open_restaurant()



wb.number_served = 15
wb.show_number_served()

wb.number_served = 42
wb.show_number_served()

wb.set_number_served(10)
wb.show_number_served()

wb.set_number_served(30)
wb.show_number_served()

wb.set_number_served(40)
wb.show_number_served()

wb.increment_number_served(5)
wb.show_number_served()

wb.increment_number_served(5)
wb.show_number_served()

wb.increment_number_served(432)
wb.show_number_served()


sal.show_number_served()

wb.describe_restaurant()


ns()

# 9-5 Login attempts

class User:
	
	def __init__(self, first_name, last_name, username, password):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.password = password
		self.login_attempts = 0

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


account = User('james', 'holt', 'jholt88', 'beetis')

account.increment_login_attempts()
print(account.login_attempts)
account.increment_login_attempts()
print(account.login_attempts)
account.increment_login_attempts()
print(account.login_attempts)

account.reset_login_attempts()
print(account.login_attempts)

