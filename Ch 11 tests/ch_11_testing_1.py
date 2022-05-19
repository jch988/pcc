

# testing a function

def get_formatted_name_1(first, last):
	"""Generate a neatly formatted full name"""
	full_name = f"{first} {last}"
	return full_name.title()

# in a separate file:

from ch_11_testing_1 import get_formatted_name

print("Enter 'q' at any time to quit")
while True:
	first = input("What is your first name? ")
	if first == 'q':
		break
	last = input("What is your last name? ")
	if last == 'q':
		break

	formatted_name = get_formatted_name(first, last)
	print(f"\tYour name is {formatted_name}")

# this works
# Want to modify function to allow middle name without affecting two-name inputs.
# But don't want to have to re-run the program every time....




# UNIT TEST
# 	- verifies that one specific aspect of a functions behaviour is correct

# TEST CASE
# 	- collection of unit tests that together prove the function works the way it's supposed to
# 	- can include all the possible kinds of input a function could receive

# Full coverage: test case that includes full range of unit tests.
# Usually, write tests for critical behaviors, and leave full coverage until widespread use



import unittest
from ch_11_testing_1 import get_formatted_name

class NamesTestCase(unittest.TestCase): 			# this class must inherit form the class unittest.Testcase
	"""Tests for 'ch_11_testing.py'."""

	def test_first_last_name(self):					# any methods with 'test_' will be run automatically when the file runs
		"""Do names like 'Janis Joplin' work?"""
		formatted_name = get_formatted_name('janis', 'joplin')	# call the function you want to test
		self.assertEqual(formatted_name, 'Janis Joplin')	# the .assert() method verifies that the result you receive is the result you expected to receive
															# check that the value from 'name' is equal to 'Janis Joplin'

if __name__ == '__main__':	# __name__ is set as '__main__' when the program is executed as the main program
	unittest.main()			# runs the test case


# Ran it, but had to put 'q'. Apparently the program runs first? Had to do it in Terminal
	# >>> .
	# >>> ----------------------------------------------------------------------
	# >>> Ran 1 test in 0.001s

	# >>> OK

# the first '.' means that a single test passed
# 'OK' tells us that all unit tests in this test case passed

# Now we know that this functions works for name inputs like that
# Can return later and make sure it still works like this after modifying to allow a middle name


# What a FAILED test looks like:

# modified to include a middle name, but the unit test from above is run as is
def get_formatted_name_2(first, middle, last):
	"""Generate a neatly formatted full name"""
	full_name = f"{first} {middle} {last}"
	return full_name.title()

# >>> E
# >>> ======================================================================
# >>> ERROR: test_first_last_name (__main__.NamesTestCase)
# >>> Do names like 'Janis Joplin' work?
# >>> ----------------------------------------------------------------------
# >>> Traceback (most recent call last):
# >>>   File "/Users/JCH/Python/pcc/Ch 11/ch_11_test_name_function.py", line 9, in test_first_last_name
# >>>     name = get_formatted_name_2('janis', 'joplin')
# >>> TypeError: get_formatted_name_2() missing 1 required positional argument: 'last'
# >>> 
# >>> ----------------------------------------------------------------------
# >>> Ran 1 test in 0.001s
# >>> 
# >>> FAILED (errors=1)



# Need to change the function to make the middle name optional

def get_formatted_name_2(first, last, middle = ''):
	"""Generate a neatly formatted full name"""
	full_name = f"{first} {middle} {last}"
	return full_name.title()

# >>> F
# >>> ======================================================================
# >>> FAIL: test_first_last_name (__main__.NamesTestCase)
# >>> Do names like 'Janis Joplin' work?
# >>> ----------------------------------------------------------------------
# >>> Traceback (most recent call last):
# >>>   File "/Users/JCH/Python/pcc/Ch 11/ch_11_test_name_function.py", line 10, in test_first_last_name
# >>>     self.assertEqual(name, 'Janis Joplin')
# >>> AssertionError: 'Janis  Joplin' != 'Janis Joplin'
# >>> - Janis  Joplin
# >>> ?      -
# >>> + Janis Joplin



# Almost. Need to write an IF block for the middle name.



def get_formatted_name_2(first, last, middle = ''):
	"""Generate a neatly formatted full name"""
	if middle:
		full_name = f"{first} {middle} {last}"
	else:
		full_name = f"{first} {last}"
	return full_name.title()

# Run same unit test...

# >>> .
# >>> ----------------------------------------------------------------------
# >>> Ran 1 test in 0.000s
# >>> 
# >>> OK

# Good!


# Check if it works for a middle name, too...

# add extra similar function to take care of that scenario

import unittest
from name_function import get_formatted_name_2

class NamesTestCase(unittest.TestCase):
	"""Tests for 'ch_11_testing.py'."""

	def test_first_last_name(self):			
		"""Do names like 'Janis Joplin' work?"""
		name = get_formatted_name_2('janis', 'joplin')
		self.assertEqual(name, 'Janis Joplin')

	def test_first_last_middle_name(self):			# remember, method name must start with test_
		"""Do names like John Paul Jones work?"""
		name = get_formatted_name_2('john', 'jones', 'paul')
		self.assertEqual(name, 'John Paul Jones')

if __name__ == '__main__':
	unittest.main()

# >>> ..
# >>> ----------------------------------------------------------------------
# >>> Ran 2 tests in 0.000s
# >>> 
# >>> OK