def new_section():
	print()
	print('---------')
	print()


# Passing an arbitrary number of arguments

# don't know how many arguments?
# use a * in the parameter
# makes an empty tuple, puts whatever values received into it

def make_pizza(*toppings):
	print("\nAdding the following toppings:")
	for topping in toppings:
			print(f"\t-{topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'extra cheese', 'pineapple')


new_section()

# if there is more than one parameter,
# the parameter accepting multuple inputs must be last in the function definition

def make_pizza_2(size, *toppings):
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"\t-{topping}")

make_pizza_2(12, 'mushrooms', 'onions', 'ham')
make_pizza_2(18, 'pineapple')
make_pizza_2(18, 'none')
make_pizza_2(16, 'green peppers', 'extra cheese')

# *args?


new_section()


# unsure of how many arbitrary argument types there will be? Use **
# this creates an empty dictionary with that name. Adds key-value pairs
# this will accept as many key-value pairs as the argument provides

def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user"""
	user_info['first name'] = first
	user_info['last name'] = last
	return user_info

	# the dictionary USER_INFO is created
	# any arbitraty arguments in the function call are added to 'user_info'
	# the function now adds 'first name' and 'last name' to 'user_info'

user_profile_aeinstein = build_profile('albert', 'einstein', location='princeton', field='physics')
user_profile_jholt = build_profile('james', 'holt', location='texas', field='science', age=33)
user_profile_teddy = build_profile('theodore', 'roosevelt', location='new york', field='politics', died=1918)

print(user_profile_aeinstein)
print(user_profile_jholt)
print(user_profile_teddy)

# notice that 'first name' and 'last name' appear last in the dictionary
# this is bc they were added to the dictionary 'user_info' after it was created




# **kwargs?


