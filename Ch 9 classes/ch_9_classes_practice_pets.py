

class Pet:

	number_of_pets = 0
	pet_list = []
	graveyard = []

	def __init__(self, name, age, color):
		self.name = name.title()
		self.age = age
		self.color = color

		Pet.pet_list.append(self.name)
		Pet.number_of_pets += 1

	def greet_pet(self):
		print(f"Hi {self.name}!")

	def list_pets():
		if len(Pet.pet_list) == 1:
			print(f"There is currently {len(Pet.pet_list)} pet:")
			for pet in Pet.pet_list:
				print(f"\t{pet}")
		elif len(Pet.pet_list) > 1:
			print(f"There are currently {len(Pet.pet_list)} pets:")
			for pet in Pet.pet_list:
				print(f"\t{pet}")

	def remove_pet(self):
		print(f"{self.name} is no longer with us 😢")
		Pet.pet_list.remove(self.name)
		Pet.graveyard.append(self.name)
		Pet.list_pets()

	def list_all_pets():
		print(f"In total, we have had {Pet.number_of_pets} pets")
		for pet in Pet.graveyard:
			print(f"\t{pet} - RIP")
		for pet in Pet.pet_list:
			print(f"\t{pet}")

	def birthday(self):
		self.age += 1
		print(f"It is {self.name}'s birthday! {self.name} is now {self.age} years old")


class Dog(Pet):

	def __init__(self, name, age, color, breed, size):
		super().__init__(name, age, color)

		self.color = color
		self.breed = breed
		self.size = size

		Dog.describe_dog(self)
		Pet.greet_pet(self)
		Pet.list_pets()

	def describe_dog(self):
		print(f"{self.name} is a {self.age}-year-old {self.size} {self.color} {self.breed}")


class Cat(Pet):

	def __init__(self, name, age, color, breed, size):
		super().__init__(name, age, color)

		self.color = color
		self.breed = breed
		self.size = size

		Pet.greet_pet(self)
		Pet.list_pets()
		

class Hedgehog(Pet):

	def __init__(self, name, age, color):
		super().__init__(name, age, color)

		if self.age == 1:
			print(f"{self.name} is {self.age} year old and is a Hedgehog!!!")
		elif self.age > 1:
			print(f"{self.name} is {self.age} years old and is a Hedgehog!!!")

		Pet.greet_pet(self)
		Pet.list_pets()


dino = Dog('dino', 14, 'white', 'terrier', 'small',)
pichu = Dog('pichu', 12, 'gray', 'snauzer', 'small')
hubert = Cat('hubert', 4, 'orange', 'bobtail', 'fat')
tex = Dog('tex', 2, 'black', 'retriever', 'medium')
ruka = Dog('ruka', 2, 'brown', 'retriever', 'medium')
frank = Hedgehog('frank', 1, 'white')

dino.remove_pet()

Pet.list_all_pets()

frank.birthday()
frank.birthday()
frank.birthday()
frank.birthday()
frank.birthday()
frank.birthday()

frank.remove_pet()

Pet.list_all_pets()


print(Pet.graveyard)