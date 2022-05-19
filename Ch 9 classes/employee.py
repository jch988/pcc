class Employee:

	raise_amt = 1.04   #class variables apply to all instances
	num_of_emps = 0
	emp_list = []

	def __init__(self, fname, pay):		#special method to initialize attributes
		self.name = fname.title()
		self.pay = pay
		self.days_on_job = 0 		#can set attributes without passing them

		Employee.num_of_emps += 1
		Employee.emp_list.append(self.name)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)
		print(f"{self.name} pay: ${self.pay}")

	def add_days(self, days):
		self.days_on_job += days

	def change_raise_amt(new_raise_amt):
		print(f"The old raise amount was {Employee.raise_amt}")
		Employee.raise_amt = new_raise_amt
		print(f"All employees will now be getting {Employee.raise_amt}")


class Developer(Employee):		# sublcass / child class

	raise_amt = 1.1  #only affects instances created from this subclass

	def __init__(self, fname, pay, lang):	# to pass new info for this subclass
		super().__init__(fname, pay)		# let the parent class handle this
		self.prog_lang = lang



james = Employee('james', 78_000)    #instance variables
chris = Employee('chris', 78_000)
eric = Developer('eric', 78_000, 'python')   #this sublcass req's additional arg

print(Employee.num_of_emps)
print(Employee.emp_list)

james.pay = 80_000		# can change attributes to modify an instance

print(james.raise_amt)
Employee.change_raise_amt(1.06)
print(james.raise_amt)

james.apply_raise() # 1.04
chris.apply_raise() # 1.04
eric.apply_raise()	# 1.1



print(james.days_on_job)
james.add_days(5)
print(james.days_on_job)

print(help(Developer))