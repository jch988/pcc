from new_section import new_section as ns

# 9-6 Ice Cream Stand

class Restaurant():

	def __init__(self, name, cuisine_type):
		self.name = name
		self.type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Displays the name and type of food"""
		print(f"The name of the restaurant is {self.name}")
		print(f"The type of food at {self.name} is {self.type}")

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


class IceCreamStand(Restaurant):
	"""A special type of restaurant that serves frozen sugar"""

	def __init__(self, name, cuisine_type):
		"""Initialize the attributes from the restaurant class"""
		super().__init__(name, cuisine_type)
		"""Add attributes specific to IceCreamStand"""
		self.flavors = []

	def flavors_add(self, addition):
		"""Add to the list of the flavors the ice cream restaurant has"""
		self.flavors.append(addition)
		print(f"\n{addition.upper()} is now on the list!")
		
		if len(self.flavors) >= 3:
			IceCreamStand.flavors_display(self)
	
	def flavors_remove(self, removal):
		"""Removes a flavor from the list"""
		self.flavors.remove(removal)
		print(f"\nRemoving {removal.upper()} from the list")
		IceCreamStand.flavors_display(self)

	def flavors_display(self):
		"""Prints out the flavors"""
		print(f"We currently have the following flavors:")
		if self.flavors == []:
			print("\t- None. Add some!")
		else:
			for flavor in self.flavors:
				print(f"\t-{flavor.title()}")

ice_cream = IceCreamStand('Creamy Sugar', 'ice cream')

ice_cream.describe_restaurant()
ice_cream.open_restaurant()
ice_cream.show_number_served()


ice_cream.flavors_display()

ice_cream.flavors_add('chocolate')
ice_cream.flavors_add('vanilla')
ice_cream.flavors_add('strawberry')
ice_cream.flavors_add('banana')

ice_cream.increment_number_served(27)
ice_cream.show_number_served()

ice_cream.flavors_remove('vanilla')

ice_cream.increment_number_served(433)
ice_cream.show_number_served()

ice_cream.flavors_remove('chocolate')
ice_cream.flavors_remove('strawberry')
ice_cream.flavors_remove('banana')


ns()


# 9-7 Admin


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



class Admin(User):
	"""A special type of User"""

	def __init__(self, first_name, last_name, username, password):
		"""Initialize the attributes from the parent class User"""
		super().__init__(first_name, last_name, username, password)
		"""Add attributes specific to Admin"""
		self.privileges = Privileges()


	# def show_privileges(self):
	# 	"""Displays the Admin's set of privileges"""
	# 	print(f"{self.username} is an Admin. The Admin privileges are:")
	# 	for item in self.privileges:
	# 		print(f"\t-{item}")


ns()

# 9-8 Privileges

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
teddy = User('teddy', 'roosevelt', 'teddy', 'bigstick')

jholt88.describe_user()
jholt88.privileges.show_privileges()
print(type(jholt88))
print(isinstance(jholt88, Admin))

wbrimley.describe_user()
wbrimley.show_privileges()
print(type(wbrimley))
print(isinstance(wbrimley, Admin))

teddy.describe_user()
teddy.show_privileges()
print(type(teddy))
print(isinstance(teddy, Admin))


ns()

# 9-9 Battery Upgrade

class Car:
	"""A simple representation of a car"""

	def __init__(self, make, model, year):
		"""Initialize attributes to create a car"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly-formatted descriptive name"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name

	def read_odometer(self):
		"""Print a statement showing the car's mileage"""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""Set the odometer reading to a given value"""
		"""Reject the change if it attempts to roll the odometer back"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the odometer!")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading"""
		if miles >= 0: 
			self.odometer_reading += miles
		else:
			print("You can't roll back the odometer!")

	def fill_gas_tank(self):
		"""Tell the owner to fill up the gas tank"""
		print("Fill up the gas tank!")


class Battery:
	"""A simple attempt to model a battery for an electric car"""

	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size"""
		print(f"This car has a {self.battery_size}-kWh battery")

	def get_range(self):
		"""Print a statement about the range this battery provides"""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"This car can go about {range} miles on a full charge")

	def upgrade_battery(self):
		"""Sets it to 100"""
		self.battery_size = 100
		print(f"The battery size is now {self.battery_size}")


class ElectricCar(Car):
	"""Represents aspects of a car specific to electric vehicles"""

	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class"""
		super().__init__(make, model, year)
		self.battery = Battery()

	def fill_gas_tank(self):
		"""Electric cars don't need gas"""
		print("Electric cars don't need gas!")


car = ElectricCar('Tesla', 'Roadster', '2022')
print(car.get_descriptive_name())

car.battery.describe_battery()
car.battery.get_range()

car.battery.upgrade_battery()

car.battery.describe_battery()
car.battery.get_range()
