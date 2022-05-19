from new_section import new_section as ns

# Object-oriented programming
# - write CLASSES that represent real-world things and situations
# - create OBJECTS based on those clasees

# Instantation - making an object from a class
# make "instances" of that class


# no () since we are creating from scratch
# class names are upper-case by convention
class Dog:
	"""A simple attempt to model a dog"""

# a function that is part of a class is called a METHOD
# the __init__ method is special,
# 	Python runs it automatically whenever we create a new instance based on the dog class
	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.name = name.title()	# these are ATTRIBUTES
		self.age = age		# attributes with .self prefix are available to every method in the class
		print(f"Hi {self.name}!")

	def sit(self):
		"""Simulate a dog sitting in reponse to a command"""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command"""
		print(f"{self.name} rolled over!")


# a class is a set of instructions for how to make an instance

my_dog = Dog('willie', 6)		# a single INSTANCE created from the class

print(f"My dog's name is {my_dog.name}")	# access the attributes
print(f"My dog is {my_dog.age} years old")

my_dog.sit()		# call a method
my_dog.roll_over()

print()

your_dog = Dog('dino', 12)		# a separate instance with its own attributes

print(f"Your dog's name is {your_dog.name}")
print(f"{your_dog.name} is {your_dog.age} years old")
your_dog.sit()
your_dog.roll_over()


lola = Dog('lola', 7)
sprocket = Dog('sprocket', 5)

print(f"My mother's dogs are {lola.name} and {sprocket.name}, "
f"who are {lola.age} and {sprocket.age} years old, respectively")

lola.sit()
lola.roll_over()

