from new_section import new_section as ns


class Car:
	"""A simple representation of a car"""

	def __init__(self, make, model, year):
		"""Initialize attributes to create a car"""
		self.make = make.title()
		self.model = model.title()
		self.fullname = self.make + ' ' + self.model
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

	def __init__(self, battery_size):
		"""Initialize the battery's attributes"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size"""
		print(f"The car has a {self.battery_size}-kWh battery")

	def get_range(self):
		"""Print a statement about the range this battery provides"""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		
		print(f"The car can go about {range} miles on a full charge")


class ElectricCar(Car):
	"""Represents aspects of a car, specific to electric vehicles"""

	def __init__(self, make, model, year, battery_size=75):
		"""Initialize attributes of the parent class"""
		"""Battery size is in kWh"""
		super().__init__(make, model, year)
		self.battery = Battery(battery_size)

	def fill_gas_tank(self):
		"""Electric cars don't need gas"""
		print("Electric cars don't need gas!")

	def __str__(self):
		return f"{self.make} {self.model}"




my_civic = Car('Honda', 'Civic', 2006)
my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_civic.get_descriptive_name())
print(my_tesla.get_descriptive_name())

my_civic.fill_gas_tank()
my_tesla.fill_gas_tank()

ns()

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

cybertruck = ElectricCar('Tesla', 'Cybertruck', 2021, 100)
print(cybertruck.get_descriptive_name())
cybertruck.battery.describe_battery()
cybertruck.battery.get_range()

