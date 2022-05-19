# Return values


# functions can process input and 'return' a value

def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted"""
	full_name = f"{first_name} {last_name}"

	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')

print(musician)

# the 'full_name' variable is returned to the function call, and can be used
# the returned value must be assigned to a variable. In this case, 'musician'


# can make certain values optional

def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted"""
	if middle_name:	     							#if middle_name = True
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()
musician = get_formatted_name('Paul', 'McCartney')
print(musician)
musician = get_formatted_name('stevie', 'vaughn', 'ray')
print(musician)

# middle_name is optional, so must be last parameter and argument


print()


# return a dictionary
# then can do more than just print. Can add to it and use it later.

def build_person(first_name, last_name, age=None):  #None is a placeholder. I guess it works the same at "" ????
	"""Return a dictionary of information about that person"""
	person = {'first': first_name, 'last': last_name,}	#this is a dictionary
	if age:
		person['age'] = age
	return person
musician = build_person('geddy', 'lee', 68)
print(musician)
musician = build_person('john', 'myung')
print(musician)

print()


# can combine functions with all Python syntax
# here is a function in use with a WHILE loop

def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

while True:
	print("Please tell me your name. \n(enter 'q' to quit)")
	f_name = input("First name: ")
	if f_name == 'q':
		print("Ok, see you later")
		break
	l_name = input("Last name: ")

	formatted_name = get_formatted_name(f_name, l_name)
	print(f"Hello {formatted_name}!\n")
	
# this would work here, too:
	# next = input("Would you like to continue? (y/n) ")
	# if next == 'y':
	# 	continue
	# if next == 'n':
	# 	print("Ok, see you later!")
	# 	break


# REVISIT 8-8, WHICH USES THIS

