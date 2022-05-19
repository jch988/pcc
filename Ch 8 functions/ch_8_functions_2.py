# Passing arguments


# 'POSITIONAL ARGUMENTS' are matched up to the corresponding parameter
# order matters

def describe_pet(animal_type, pet_name):
	"""Display information about a pet"""
	print(f"I have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.\n")

describe_pet('dog', 'dino')
describe_pet('dog', 'pichu')
describe_pet('cat', 'hubert')
describe_pet('hamster', 'harry')
describe_pet('frank', 'hedgehog')	# wrong order. Messes up the output

# can use as many positional arguments as you want

print()

# A 'KEYWORD ARGUMENT' is a name-value pair that you pass to the function
# order doesn't matter

describe_pet(animal_type='dog', pet_name='lola')
describe_pet(pet_name='sprocket', animal_type='dog') # reversed. Doesn't matter
describe_pet(animal_type='cat', pet_name='hubert')


print()
print("-------------")

# default values can be used if many of the arguments will be the same
# *!* the parameters that require input need to come first *!*

def describe_pet(pet_name, animal_type='dog'):
	print(f"I have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.\n")

describe_pet('willie')


# can still set a different value in the argument (reverts after)

def fav_book(book_title, genre='fiction'):
	print(f"Recently I have read {book_title}")
	print(f"It is a work of {genre}.\n")

fav_book('The Way of Kings')
fav_book('The Expanse')
fav_book('Extreme Ownership', genre='non fiction')	# default val is ignored
fav_book('Snow Crash')								# un-ignored



print()


# there are often multiple equivalent ways to call a function.
# use the style you find easiest to understand

describe_pet('willie')
describe_pet(pet_name='willie')
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


print()


# describe_pet() doesn't work bc there are no arguments















