# LOOPING THROUGH A DICTIONARY

# can loop through key:value pair, just the keys, or just the values

user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
}


for key, value in user_0.items():
	print(f"Key: {key}")
	print(f"Value: {value}\n")
# names were created to hold each key:value pair
# any names would work, not just 'key' or 'value'

# the method .items() returns a list of key:value pairs


favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite programming language is {language.title()}.")


print()


# can loop through just all the keys
# use .keys() instead of .items()

for name in favorite_languages.keys():
	print(name.title())

print()

# also...
for name in favorite_languages:
	print(name.title())

# ...'keys' is actually the defalt behaviour for looping through a dictionary if no method is attached
# putting 'keys()' might make the code easier to read


print()

# can access the value associated with any key while in a loop

friends = ['phil', 'sarah']

for person in favorite_languages.keys():
	print(f"Hi {person.title()}")

	if person in friends:
		language = favorite_languages[person].title() #determine person's fav lang using dict name and 'name' label assigned
		print(f"\t{person.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")


print()

# can loop through the keys in a particular order
# not just the order in which they are entered
# use 'sorted()' from ch.3

print("In alphabetical order:")
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")

print("\nNow in reverse alphabetical order!")
for name in sorted(favorite_languages.keys(), reverse=True):
	print(f"{name.title()}, thank you for taking the poll.")


print()

persons = ['erin', 'steve', 'edward']

for person in persons:
	if person not in favorite_languages.keys():
		print(f"{person.title()}, please take our poll!")
	else:
		print(f"{person.title()}, thank you for taking our poll.")
	if person == 'steve':
		print("\tWhat kind of rapping name is that, anyway?")

print()


# what if you're interested in just the values?
# use .values()

print("The following languages have been mentioned:")
for language in sorted(favorite_languages.values()) :
	print(language.title())

# but there are duplicates here. We don't need them.
# wrap a set() around the list to remove them
# a SET is a collection in which each item must be unique

print()

print("Now, without duplicates:")
for language in set(favorite_languages.values()):
	print(language.title())
