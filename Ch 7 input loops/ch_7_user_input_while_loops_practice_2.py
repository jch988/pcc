
# 7-4 Pizza Toppings

prompt = "\nWhat would you like on your pizza?"
prompt += "\n(When you are done adding, say 'done') "
toppings = ""

while toppings != 'done':
	toppings = input(prompt)
	print(f"\nOkay, I'll add {toppings}.")
	if toppings == 'done':
		print("\nLooks like you're finished adding. We'll start making it.")


print()


# 7-5 Movie Tickets

# age < 3: free
# age <= 12: $10
# age > 12: $15

question = "\nWhat is your age? (Let me know when you're 'done') "
age = ""

while age != 'done':
	age = (input(question))
	if age != 'done' and int(age) < 3:
		print("You get in for free!")
	elif age != 'done' and int(age) <= 12:
		print("Your cost is $10")
	elif age != 'done' and int(age) > 12:
		print("That will be $15, please")

# I think this is ugly af, but it works.


# 7-6 
# Write different versions of 7-4 and/or 7-5 that do each of the following at least once:
# 	Use a conditional test in the while statement to stop the loop
# 	Use an ACTIVE variable (a FLAG)
# 	Use a BREAK statement




order = "\nWhat would you like on your pizza? Say 'none' if you're finished "

active = True
while active:
	toppings = input(order)
	if toppings == 'none':
		print("Ok, we'll get started on making that")
		active = False
	else:
		print(f"Adding {toppings}!")




question = "\nWhat is your age? (To get me to stop asking, type 'quit') "
age = ""

while age != 'quit':
	age = input(question)
	if age == 'quit':
		print("ok, we're done here")
		break
	if age != 'done' and int(age) < 3:
		print("You get in for free!")
	elif age != 'done' and int(age) <= 12:
		print("Your cost is $10")
	elif age != 'done' and int(age) > 12:
		print("That will be $15, please")



print()


# 7-7 

# create an infinite loop

# I've done plenty of that by accident already