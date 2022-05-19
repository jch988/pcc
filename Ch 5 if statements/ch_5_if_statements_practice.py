# 5-1 Conditional Tests
# Write a series of conditional tests. Print a statement describing each result

coffe_maker = 'french_press'
print("Is coffe_maker == 'french_press'?. I predict True")
print(coffe_maker == 'french_press')
print("Is coffe_maker == 'drip'? I think not")
print (coffe_maker == 'drip')


print()


# 5-2 More conditional tests

computer = 'macbook_air'
print(computer == 'pc')
print(computer == 'macbook_air')



# 5-3 Alien colors

alien_colors = ['green', 'red', 'yellow']
alien_color = 'blue'

if alien_color == 'green':
	print("The alien is green. You earned 5 points!")
if alien_color == 'yellow':
	print("That's the yellow alien. 10 points!")
if alien_color == 'red':
	print("The the red alien. 15 points")

print()

# 5-4 Alien colors 2
if alien_color == 'green':
	print("You got a green alien! That's 5 points for you")
else:
	print("That's not the green alien. You've earned 10 points!")


# 5-5 Alien colors 3
if alien_color == 'green':
	score = 5
elif alien_color == 'yellow':
	score = 10
else:
	score = 15
print(f"You got the {alien_color} alien, that's worth {score} points!")


# 5-6
# write an if-elif-else statement about a person's stage of life

age = 33
stages = ['baby', 'toddler', 'kid', 'teenager', 'adult', 'elder']

if age < 2:
	stage = 'baby'
elif age < 4:
	stage = 'toddler'
elif age < 13:
	stage = 'kid'
elif age < 20:
	stage = 'teenager'
elif age < 65:
	stage = 'adult'
else:
	stage = 'elder'
print(f"Since your age is {age}, your stage of life is '{stage}'")

print()

# 5-7 Favorite Fruit

fav_fruits = ['bananas', 'mangoes', 'blueberries']
if 'bananas' in fav_fruits:
	print("Bananas are among my favorite fruits")
if 'papayas' in fav_fruits:
	print("Papayas are great!")
if 'mangoes' in fav_fruits:
	print("I like mangoes")
if 'avocados' in fav_fruits:
	print("I enjoy eating avocados")
if 'blueberries' in fav_fruits:
	print("Blueberries are the best!")

print()


# 5-8 Hello Admin

user_names = ['jch', 'admin', 'alias', 'handle', 'login', 'user1']

for user in user_names:
	if user == 'admin':
		print(f"Hello {user}, would you like to see a status report?")
	else:
		print(f"Hello {user}, welcome")

print()

# 5-9 No users

# add an if-test to see if the list contains any users at all

# user_names = ['jch', 'admin', 'alias', 'handle', 'login', 'user1']
user_names = []

if user_names:
	for user in user_names:
		if user == 'admin':
			print(f"Hello {user}, would you like to see a status report?")
		else:
			print(f"Hello {user}, welcome")
else:
	print("No one has logged in. We need to find some users!")


print()

# 5-10 Checking usernames
# how websites ensure that everyone has a unique username

current_users = ['wilford', 'brimley', 'Beetis', 'check', 'sugar']
new_users = ['testing', 'supplies', 'beetis', 'call liberty', 'Sugar']

# LIST COMPREHENSION to change all input to lowercase to make sure there are no duplicates
current_users_lower = [name.lower() for name in current_users]
new_users_lower = [name.lower() for name in new_users]

for new_user in new_users_lower:
	if new_user in current_users_lower:
		print(f"Sorry, {new_user} is already taken. Please choose another name")
	else:
		print(f"Hi, {new_user}, welcome to the website!")


print()

# 5-11 Ordinal Numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
	if num == 1:
		print(f"{num}st")
	elif num == 2:
		print(f"{num}nd")
	elif num == 3:
		print(f"{num}rd")
	else:
		print(f"{num}th")



