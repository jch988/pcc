def new_section():
	print()
	print('---------')
	print()


# Storing functions in modules

# Can store a function in a separate file called a 'module' and then 'import' it
# - hide details
# - focus on different things
# - can share just the function without sharing the entire program
# - can import other programmer's functions

# MODULE - file ending in .py that contains the code you want to import

# there are different ways to do this

new_section()
# ---------------------------

# IMPORTING AN ENTIRE MODULE:

import ch_8_functions_modules_pizza
# must be in same directory
# any function defined in that file is now available in this one

# use dot notation to call a function
ch_8_functions_modules_pizza.make_pizzas(16, 'pepperoni')
ch_8_functions_modules_pizza.make_pizzas(18, 'peppers', 'onions')


new_section()
# -------------------

# IMPORTING SPECIFIC FUNCTIONS

from ch_8_functions_modules_pizza import make_pizzas, greet_user

# no need for the dot notation
greet_user('james')


new_section()
# -----------------------

# IMPORT USING AN ALIAS

# if the function name is long or might conflict with an existing name

from ch_8_functions_modules_pizza import greet_user as greet

greet('martha')


new_section()
# -------------------------

# GIVE A MODULE AN ALIAS

import ch_8_functions_modules_pizza as mod

mod.fun1()




new_section()
# --------------------

# IMPORT ALL FUNCTIONS IN A MODULE

from ch_8_functions_modules_pizza import *

# each function is imported, so don't need the dot notation
fun2()

# don't use this when working with large modules you didn't write

# best approach: import just the functions you want
# or import the entire module and use dot notation
# This will result in code that is clear and easy to read and understand


