# using IF statements with lists

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	print(f"Adding {requested_topping}.")
print("Finished making your pizza!")


print()

# what if the green peppers run out?
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers")
	else:
		print(f"Adding {requested_topping}.")
print("Finished making your pizza!")
# the if-else loop allows for a special statement to be made


print()

# What if someone doesn't want any toppings?	requested_toppings = []
# In other words, the list will be empty
# The code above will just print "Finished making your pizza!" if requested_toppings = []
# We need a little more in that case

requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		if requested_topping == 'green peppers':
			print("Sorry, we are out of green peppers")
		else:
			print(f"Adding {requested_topping}.")
else:
	print("Are you sure you want a plain pizza?")

# the FOR loop only matters if someone wants toppings. This checks to see if the list has something
# When the name of the list is used in an IF statement, Python returns TURE if the list has something
# if the list passes the conditional test, the indented part begins running
# if not, it's FALSE and the ELSE statement applies

print()

# What if someone wants something unavailable, like fries?
# We check the request against what's available

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 
					'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}")
	else:
		print(f"Sorry, we don't have {requested_topping}")
print("Finished making your pizza!")



