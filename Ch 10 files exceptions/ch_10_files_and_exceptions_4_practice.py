from new_section import new_section as ns

# 10-11 Favorite Number

import json
fav_num = input("What is your favorite number? ")
filename = 'ch_10_fav_num.json'
with open(filename, 'w') as f:
	json.dump(fav_num, f)

import json
filename = 'ch_10_fav_num.json'
with open(filename) as f:
	answer = json.load(f)
print(answer)


ns()

# 10-12 Fav Num Remembered

import json
filename = 'ch_10_fav_num.json'
try:
	with open(filename) as f:
		answer = json.load(f)
except FileNotFoundError:
	answer = input("What is your favorite number? ")
	with open(filename, 'w') as f:
		json.dump(answer, f)
		print(f"I will remember that {answer} is your favorite number")
else:
	print(f"Your favorite number is {answer}")


ns()

# 10-13 Verify User

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
	print(f"I will remember that, {username}")			# moved this from the else block of greet_user()
	return username

def greet_user():
	"""Greet user by name"""
	username = get_stored_username()
	if username:
		verify = input("Let's verify. What is your username? ")		#to verify that it's the right user
		if verify == username:
			print(f"Welcome back, {username}")
		else:
			print("Sorry, that is not the correct username. Let's get you set up.")
			get_new_username()
	else:
		username = get_new_username()

greet_user()

