class Employee:

	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = salary

	def give_raise(self, amount=5_000):
		self.salary += amount
