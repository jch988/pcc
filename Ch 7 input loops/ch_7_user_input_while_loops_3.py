# Using a while loop with Lists and Dictionaries

# use a WHILE loop instead of FOR loop to modify a list while working with it

# here, will move items from one list to another

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:   #runs as long as the unconfirmed_users is not empty
	current_user = unconfirmed_users.pop()

	print(f"Verifying user: {current_user.title()}")
	confirmed_users.append(current_user)

print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())


print()


# can use a WHILE loop to remove all instances of an element from a list

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)

# the remove() method would not work as well because 'cats' appears multiple times


print()


# Use a while loop to populate a dictionary with user input

responses = {}				# creates dictionary 

polling_active = True		# set flag to indicate polling is active

while polling_active:		# this will loop until the flag turns False
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")

	responses[name] = response     # adds key-value pair to dictionary

	repeat = input("Would you like to let another person respond? (y/n) ")
	if repeat == 'n':
		polling_active = False

print("\n------- Poll Results ------")
for name, response in responses.items():    # recalls the key-value pairs added previously
	print(f"{name} would like to climb {response}.")


# JCH note: this works, but if two people enter the same name, only the second one shows in the results








