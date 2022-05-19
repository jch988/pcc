# Nesting

# store multiple dictionaries in a list. Or store a list if items as a value in a dictionary


# A LIST OF DICTIONARIES

# here is a dictionary:
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# this list contains the dictionary of each alien
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

print()


# expand this:

aliens = []

for alien_number in range(30):   # for 30 times...
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}  # creates a new alien
	aliens.append(new_alien)	# adds the new alien to the list

# just populated the above list with 30 aliens!

for alien in aliens[:5]:  # just want to view the first five, so we include that SLICE in the FOR loop
	print(alien)
print("...")

print(f"Total number of aliens : {len(aliens)}")

# each of these 30 aliens is now a separate object, so can modify individually

print()


# want to change the first three to yellow, medium speed

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = '10'
		alien['speed'] = 'medium'
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['points'] = '15'
		alien['speed'] = 'fast'

for alien in aliens[:5]:
	print(alien)

# now the first 3 are yellow medium aliens, and the rest are green slow
# the elif block would turn any yellow aliens to red

# the list 'aliens' now contains a number of dictionaries


print()


# A DICTIONARY OF LISTS

pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")


print()


favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go', "c++"],
	'phil': ['python', 'haskell'],
	}


for name, languages in favorite_languages.items():	
	if len(languages) < 2:
		print(f"\n{name.title()}'s favorite language is: \n\t{language.title()}")
	else:
		print(f"\n{name.title()}'s favorite languages are:")
		for language in languages:
			print(f"\t{language.title()}")


print()

# A DICTIONARY IN A DICTIONARY

users = {
	'aeinstein': {
	'first': 'albert',
	'last': 'einstein',
	'location': 'princeton',
	},

	'mcurie': {
	'first': 'marie',
	'last': 'curie',
	'location': 'paris',
	},

}

for username, user_info in users.items():   # username & user_info is the key-value pair. user_info is itself a dictionary
	print(f"\nUsername: {username}")
	
	full_name = f"{user_info['first']} {user_info['last']}"  # looks up values for keys 'first' and 'last'
	location = user_info['location']	# looks up the value paired with key 'location' in the dictionary 'user_info'

	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")


