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