# look what I did:
def new_section():
	print()
	print("----------")
	print()
new_section()

# 8-12 Sandwiches

def make_sandwich(bread, meat, cheese, *toppings):
	# print(f"\nMaking a sandwich with {bread} bread, {meat} meat, {cheese} cheeses,"
	# " and the following toppings:")
	print("\nMaking a sandwich...")
	print(f"\tBread: {bread}")
	print(f"\tMeat: {meat}")
	print(f"\tCheese: {cheese}")
	print(f"\tToppings:")
	for topping in toppings:
		print(f"\t\t-{topping}")


make_sandwich('rye', 'pastrami', 'swiss', 'mayo', 'lettuce', 'tomato')
make_sandwich('sourdough', 'ham', 'munster', 'mustard')
make_sandwich('toast', 'none', 'cheddar', 'onions', 'more onions')


new_section()

# 8-13 User Profile

def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user"""
	user_info['first name'] = first
	user_info['last name'] = last
	return user_info


user_profile_jholt = build_profile('james', 'holt', location='texas', 
	field='science', age=33,)
print(user_profile_jholt)


new_section()


# 8-14 Cars

def build_car(make, model, **car_details):
	"""Stores information about a car in a dictionary"""
	car_details['make'] = make
	car_details['model'] = model
	return car_details

prius = build_car('toyota', 'prius', color='silver', year='2015')
subi = build_car('subaru', 'impreza', color='blue', name='tink')
print(prius)
print(subi)

