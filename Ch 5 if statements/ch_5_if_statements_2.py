# conditional tests lead directly into IF STATEMENTS

age = 19
if age >= 18:
	print("You are old enough to vote")
	print("Have you registered to vote yet?")

# the block of indented lines will be executed if the statement is true
# if false, the entire indented block will be ignored

age = 17
if age >= 18:
	print("You are old enough to vote")
	print("Have you registered to vote yet?")
	# this is all ignored. No output is produced

# if-else statements take one action if a condition passes, and a different action in all other cases
age = 17
if age >= 18:
	print("You are old enough to vote")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too youg to vote")
	print("Please register to vote as soon as you turn 18")


# if-elif-else chains test more then two possible situations
# when one conditional test passes, the code following that test is passed, and the rest of the tests are skipped

# age < 4 = free
# age 4-18 = $25
# age > 18 = $40

age = 12
if age < 4:
	print("You get in for free!")
elif age < 18:
	print("That will be $25")
else:
	print("Your price of admission is $40. Enjoy!")

# a simpler way to do this:
age = 18
if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40
print(f"Your admission cost is ${price}")
# easier to read and modify


# multiple elif blocks
age = 66
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20
print(f"Your admission cost is ${price}")


# the ELSE block is not required.
age = 4
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20
print(f"Your admission cost is ${price}")


# the ELSE block is a catch-all for anything that doesn't fit into IF or ELIF
# if there is a specific final conidition, consider omitting the ELSE and use only ELIF

# The above only work if you require a single test to pass (the rest are skipped)

# to test multiple inputs, use a series of IF statements
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese")
print("Finished making your pizza!")

# if ELIF was used in the 2nd and 3rd parts, the code would stop after the first test passed
