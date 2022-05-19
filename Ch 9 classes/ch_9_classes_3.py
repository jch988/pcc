from new_section import new_section as ns

# Inheritance

# CHILD class can take on attributes and methods of PARENT class,
# plus add others

# car class from before:

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





	# added this later as part of #2 below
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




my_civic = Car('Honda', 'Civic', 2006)

# now make ElectricCar, which can be similar to Car, with additions



# added Battery class last to offload from ElectricCar

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
			range = 200
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about {range} miles on a full charge")



# the parent class must be part of the file and must appear before the child
# The name of the parent class goes in ()


class ElectricCar(Car):
	"""Represents aspects of a car, specific to electric vehicles"""

	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class"""
		super().__init__(make, model, year)

		# special function. Calls __init__() method from parent class
		# parent is SUPERclass and child is SUBclass

		"""Initialize attributes specific to electric cars"""
		# self.battery_size = 75
		# will be associated with ElectricCar but not Car

		self.battery = Battery()
		# this attribute is now an instance from the class Battery

	# def describe_battery(self):
	# 	"""Prints a statement describing the battery size"""
	# 	print(f"This car has a {self.battery_size}-kWh battery")


# can override methods from the parent class
# just use the same name

	def fill_gas_tank(self):
		"""Electric cars don't need gas"""
		print("Electric cars don't need gas!")


# can break large classes into many smaller ones
# ex: a class for Battery might be useful






my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_civic.get_descriptive_name())
print(my_tesla.get_descriptive_name())

# my_tesla.describe_battery()

my_civic.fill_gas_tank()
my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()
# battery, and not Battery, because this tells Python to look at my_tesla, 
# which is an instance created from ElectricCar.
# self.battery is an instance in ElectricCar created from Battery.
# This calls that battery instance, not the Battery class.

my_tesla.battery.get_range()