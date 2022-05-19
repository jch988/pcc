from new_section import new_section as ns

# Storing Data

# JSON module
# 	- JavaScript Object Notation
# 	- dump simple Python data structures into a file and load that file the next time the program runs
# 	- compatible with other languages

import json

numbers = [2, 3, 5, 7, 11, 13]
random_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

filename = 'ch_10_numbers.json'
with open(filename, 'w') as f:
	json.dump(numbers, f)
# opening this in a different file...
	import json
	filename = 'ch_10_numbers.json'
	with open(filename) as f:
		numbers = json.load(f)
	print(numbers)
	# >>> [2, 3, 5, 7, 11, 13]



ns()

# save user input, recall in a different file

import json

username = input("What is your name? ")

filename = 'ch_10_username.json'
with open(filename, 'w') as f:
	json.dump(username, f)
	print(f"I will remember that name, {username}")

# in terminal:
	# What is your name? James
	# I will remember that name, James
# different file:

	import json
	filename = 'ch_10_username.json'
	with open(filename) as f:
		username = json.load(f)
		print(f"Welcome back, {username}")
	>>> Welcome back, James


ns()


# but want to combine these into the same file
# in that case will use a try-except block
# it loads the username if it has been stored previously
# otherwise, (if a FileNotFoundError comes up), it asks for the username


import json

filename = 'ch_10_username.json'

try:											# if the file exists
	with open(filename) as f:
		username = json.load(f)
except FileNotFoundError:						# runs if the file doesn't already exist
	username = input("What is your name? ")
	with open(filename, 'w') as f:
		json.dump(username, f)
		print(f"I will remember that, {username}")
else:
	print(f"Welcome back, {username}")

# when no file 'ch_10_username.json' exists...

# >>> What is your name? Wilford Brimley
# >>> I will remember that, Wilford Brimley

# run program again:
# >>> Welcome back, Wilford Brimley


ns()


# Refactoring
# 	- break the code up into a series of functions that have specific jobs

import json

def get_stored_username():
	"""Get stored username if available"""
	filename = 'ch_10_username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Prompt for a new username"""
	username = input("What is your name? ")
	filename = 'ch_10_username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username

def greet_user():
	"""Greet user by name"""
	username = get_stored_username()
	if username:
		print(f"Welcome back, {username}")
	else:
		username = get_new_username()
		print(f"I will remember that, {username}")

greet_user()

# each of these functions has a specific job 