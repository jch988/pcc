# an IF STATEMENT allows you to examine a statement and respond appropriately to the state of the program

cars = ['audi', 'bmw', 'subaru', 'toyota']

for brand in cars:
	if brand == 'bmw':
		print(brand.upper())
	else:
		print(brand.title())

# checks if the value in the list is 'bmw'. If so, prints in upper case. If not (else), prints in title case

# every if statement has a True or False, called a CONDITIONAL TEST
# if the test is true, the following code is executed
# if it isn't true, the code following the if statement is not executed

# '=' sets the value.
# '==' asks "Is this the same value?"
# case-sensitive


# != checks for inequality. The ! represents "not"
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies")

# <, <=, >, and >= can also be used in a similar way
answer = 17
if answer != 42:
	print("That is not the correct answer. Please try again!")
if answer <20:
	print("The answer is less than twenty")
if answer >=9:
	print("The answer is more than or equal to nine")
	print("the answer is definitely more than nine")


# 'in' tells you if a value is already in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
	print("Mushrooms are on the list!")
if 'pepperoni' not in requested_toppings:
	print("There will be no pepperoni")

# 'not' works as well
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish")
else:
	print(f"Sorry {user.title()}, you are banned")


# a BOOLEAN EXPRESSION is another name for Conditional Test
# it's either True or False
game_active = True
can_edit = False
# provides a way to track the state of a program, or a particular condition






