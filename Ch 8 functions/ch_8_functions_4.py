# Passing a List through a function

def greet_users(names):
	"""Print a simple greeting to each user on the list"""
	for name in names:
		msg = f"Hello {name}!"
		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# a list was used as the argument
# combined with the FOR loop in the function, this printed each name

print()

names = ['james', 'douglas', 'josie']
greet_users(names)
print()
greet_users(usernames[-1:])


print()

# a function can modify a list

# example:

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"Printing model: {current_design}")
	completed_models.append(current_design)

print(f"\nThe following models have been printed:")
for model in completed_models:
	print(f"\t{model}")

# can re-structure this with functions

print("------------")

def print_models(unprinted_designs, completed_models):
	"""Simulate printing each design, until none are left.
	Move each design to completed models after printing"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the models that were printed"""
	print(f"\nThe following models have been printed:")
	for model in completed_models:
		print(f"\t{model}")

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# now it is simpler and more organized overall
# could call in the function with a new list later
# if the code needs to change, it only has to be done once

print("------------")

next_unprinted_designs = ['notebook cover', 't-shirt', 'painting']
next_completed_models = []

print_models(next_unprinted_designs, next_completed_models)
show_completed_models(next_completed_models)

print("------------")

more_unprinted_designs = ['chair', 'water bottle', 'tool shed']
more_completed_models = []

print_models(more_unprinted_designs, more_completed_models)
show_completed_models(more_completed_models)

print("------------")
print()


# may want to prevent a fuction from modifying a list
# pass the function a COPY of the list
# function_name(list_name[:])

last_unprinted_designs = ['pen case', 'bed sheets', 'headphones']
last_completed_models = []

print(more_unprinted_designs)	#this list is empty bc it was previously depopulated
print(last_unprinted_designs)	

print_models(last_unprinted_designs, last_completed_models)	#send a copy[:]
show_completed_models(last_unprinted_designs)

print(last_unprinted_designs)	# prove that the original list is intact

# do this only when there is a specific reason to

