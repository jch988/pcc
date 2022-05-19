# A FUNCTION is a block of code designed to do one specific job
# can do that job over and over again just by calling the function name

# makes programs easier to write, read, test, and fix


# here is what a simple one looks like

def greet_user():
	"""Display a simple greeting."""
	print("Hello")

greet_user()

# 'def' informs python that you are defining a function. 'Function Definition'
# the () will hold any info needed for the function to do its job
# following indented lines make up the BODY of the function
# comment in """ is a DOCSTRING. It describes what the function does
# The FUNCTION CALL tells Python to run it. Relevant info is included in ()


# can 'pass' information through the function
def greet_user(username):				# PARAMETER
	"""Display a simple greeting"""
	print(f"Hello {username.title()}!")

greet_user('jesse')  	# funciton call
greet_user('sarah')		# gives the needed info to execute the print call
greet_user('bryan')			# ARGUMENT
greet_user('emily')
# above, 'username' is a 'PARAMETER'
# 	- a piece of info the function needs to do its job
# 'jesse'—or any of the names—is an 'ARGUMENT': 
# 	- the piece that is passed from the functional call to the function
# 	- is going to be in quotes(?)

# can call the function as many times as you want with new information

print()
print("---------------")
print()

# can call a function from another function
# side note. Found this on a website:

def fun1():
	print("Called by fun1")

def fun2():
	print("Called by fun2")
	fun1()

fun2()

# fun2() includes a call for fun1(), so both are used, even tho fun2() is the only one directly called



