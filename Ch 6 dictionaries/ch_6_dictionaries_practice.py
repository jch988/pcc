# 6-1 Person
# Use a dictionary to store information about a person you know.

douglas = {
	'first_name': 'douglas',
	'last_name': 'greenston',
	'age': '20',
	'city': 'columbia',
}

print(f"Doulgas's first name is {douglas['first_name']}")
print(f"Doulgas's last name is {douglas['last_name']}")
print(f"Doulgas's age is {douglas['age']}")
print(f"Doulgas's city is {douglas['city']}")


print()


# 6-2 Favorite Numbers
# Use a dictionary to store people's favorite numbers

fav_numbs = {
	'holly': 25,
	'douglas': 99,
	'matt': 12,
	'alex': 84,
	'jordan': 99,
}


print(f"Holly's favorite number is {fav_numbs['holly']}")
print(f"Doulgas's favorite number is {fav_numbs['douglas']}")
print(f"Matt's favorite number is {fav_numbs['matt']}")
print(f"Alex's favorite number is {fav_numbs['alex']}")
print(f"Jordan's favorite number is {fav_numbs['jordan']}")


print()


# 6-3 Glossary
# 

glossary = {
	'method': 'an action that can be performed on a piece of data',
	'import this': 'the zen of python',
	'list': 'a collection of items in an order',
	'tuple': 'an immutable list',
	'pep 8': 'Python styling guide',
}

print(f"Method: \n\t{glossary['method']}")
print(f"import this: \n\t{glossary['import this']}")
print(f"List: \n\t{glossary['list']}")
print(f"Tuple: \n\t{glossary['tuple']}")
print(f"PEP 8: \n\t{glossary['pep 8']}")


print()


# 6-4 Glossary 2
# clean up the code from 6-3 by replacing the series of print calls with a loop

for term, definition in glossary.items():
	print(f"{term.title()}: {definition}")

# now add five new terms

print()

glossary['Dictionary'] = 'A collection of key-value pairs'
glossary['Set'] = 'A collection in which each item must be unique'
glossary['String'] = 'A series of characters'
glossary['Float'] = 'Number with a decimal'
glossary['Whitespace'] = 'Any non-printing character'

for term, definition in glossary.items():
	print(f"{term.title()}: {definition}")


print()

# 6-5 Rivers

rivers = {
	'nile': 'egypt',
	'amazon': 'brazil',
	'mississippi': 'the united states',
}

for river, country in rivers.items():
	print(f"The {river.title()} river runs through {country.title()}")


for river in rivers.keys():
	print(river.title())

for country in rivers.values():
	print(country.title())


print()

# 6-6 Polling

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

poll_takers = ['sarah', 'erin', 'james', 'jen', 'david', 'amanda']

for name in poll_takers:
	if name in favorite_languages.keys():
		print(f"Thank you, {name.title()}, for taking the poll!")
	else:
		print(f"{name.title()}, please take the poll.")


print()


# 6-7 People
# start with ex 6-1


douglas = {
	'first_name': 'douglas',
	'last_name': 'greenston',
	'age': '20',
	'city': 'columbia',
}

holly = {
	'first_name': 'holly',
	'last_name': 'greenston',
	'age': '45',
	'city': 'san antonio',
}

jose = {
	'first_name': 'jose',
	'last_name': 'salas',
	'age': '42',
	'city': 'segiun',
}

people = [douglas, holly, jose]

for person in people:
	print(person.values())
	print(f"{person['first_name'].title()}'s last name is {person['last_name'].title()}, age "
	f"is {person['age']}, and current city is {person['city'].title()}\n")



print()



# 6-8 Pets

pichu = {
	'name': 'pichu',
	'kind': 'dog',
	'owner': 'matt',
}

dino = {
	'name': 'dino',
	'kind': 'dog',
	'owner': 'josie',
}

hubert = {
	'name': 'hubert',
	'kind': 'cat',
	'owner': 'holly',
}

tex = {
	'name': 'tex',
	'kind': 'dog',
	'owner': 'douglas',
}

pets = [pichu, dino, hubert, tex]

for pet in pets:
	print(f"{pet['name']} is a {pet['kind']} and belongs to {pet['owner']}")




print()


# 6-9 Favorite places

favorite_places = {
	'peggy': ['vermont', 'mountains', 'home'],
	'josie': ['england', 'new zealand'],
	'gabe': ['houston', 'beijing', 'new england'],
	'david': ['durango']
}

for person, places in favorite_places.items():
	if len(places) < 2:
		print(f"{person}'s favorite place is {places}")
	else:
		print(f"{person}'s favorite places are {places}")

print()

for person, places in favorite_places.items():
	print(f"\n{person}'s favorite places are:")
	for place in places:
		print(f"\t{place}")



print()



# 6-10 Favorite numbers
# modify 6-2 so each person can have more than one fav number

fav_numbs = {
	'holly': [25, 26],
	'douglas': [99, 362],
	'matt': [12, 14, 84],
	'alex': [84, 887, 1],
	'jordan': [99, 100],
}

for name, numbs in fav_numbs.items():
	print(f"{name}'s favorite numbers are {numbs}")



print()


# 6-11 Cities

cities = {
	'san antonio': {
	'country': 'the united states',
	'population': '1.4 million',
	'fact': 'is the oldest city in texas',
	},

	'vancouver': {
	'country': 'canada',
	'population': '600,000',
	'fact': 'has only one highway',
	},

	'ushuaia': {
	'country': 'argentina',
	'population': '56,000',
	'fact': 'is the southernmost city in the world',
	},
}

for city, city_info in cities.items():
	print(f"{city}")
	print(f"\t{city} is located in {city_info['country']}")
	print(f"\t{city} has a population of {city_info['population']}")
	print(f"\tan interesting fact about {city} is that it {city_info['fact']}!\n")



# 6-12 Extensions
# use one of the examples from this chapter and extend it by adding
# new keys and values, changing the context of the program, or improving the 
# formatting of the output

# had already done something like this
# By asking Steve what kind od rapping name that is, anyway

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

persons = ['erin', 'steve', 'edward']

for person in persons:
	if person not in favorite_languages.keys():
		print(f"{person.title()}, please take our poll!")
	else:
		print(f"{person.title()}, thank you for taking our poll.")
	if person == 'steve':
		print("\tWhat kind of rapping name is that, anyway?")



