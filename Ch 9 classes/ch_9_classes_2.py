from new_section import new_section as ns

# Modifying instances


class Car:
	"""A simple representation of a car"""

	def __init__(self, make, model, year):
		"""Initialize attributes to create a car"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0   # added this attribute which changes over time


	def get_descriptive_name(self):
		"""Return a neatly-formatted descriptive name"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name


	def read_odometer(self):
		"""Print a statement showing the car's mileage"""
		print(f"This car has {self.odometer_reading} miles on it.")


# so far can show what kind of car there is


	# added this later as part of #2 below
	def update_odometer(self, mileage):
		"""Set the odometer reading to a given value"""
		# self.odometer_reading = mileage

		"""Reject the change if it attempts to roll the odometer back"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the odometer!")


	# added as part of #3 below
	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading"""
		if miles >= 0: 
			self.odometer_reading += miles
		else:
			print("You can't roll back the odometer!")





car = Car('Toyota', 'Prius', 2015)

print(car.get_descriptive_name())
print(f"The car is a {car.get_descriptive_name()}")

car.read_odometer()

# want to modify the odometer reading. Three ways:
# 	1 - Directly thorugh an instance
# 	2 - set it with a method
# 	3 - increment through a method

# 1
car.odometer_reading = 23
car.read_odometer()		# prints "The car has 23 miles on it"

# 2
# added def update_odometer(self, mileage)
car.update_odometer(24)
car.read_odometer()

# added the if-else block to def update_odometer
car.update_odometer(19) # prints "You can't roll back the odometer!"
car.update_odometer(25)
car.read_odometer()

# 3
# added def increment_odometer(self, miles)
car.increment_odometer(100)
car.read_odometer()
car.increment_odometer(500)
car.read_odometer()

