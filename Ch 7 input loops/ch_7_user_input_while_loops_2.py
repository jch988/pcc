# WHILE LOOPS

# runs as long as a cetain condition is true

current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1    # += 1 means add 1... current_number = current_number + 1

print()

prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""    #this is so python has something to check the first time

while message != "quit":
	message = input(prompt)
	print(message)

# (?? what if I want Quit or QUIT or any capitalized form of 'quit' to work ??)



# don't want it to print the word 'quit' 

prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != 'quit':
	message = input(prompt)
								#removed print(message)

	if message != 'quit':
		print(message)
# now it just stops when 'quit' is entered




print()


# it becomes complicated to test many conditions in a single WHILE statement

# a FLAG is a variable that signals whether or not the entire program is active
# set program to run while flag is TRUE and stop when it is FALSE
# a flag can be called anything

prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True								# 'active' is the FLAG.
while active:								# as long as active = True, the while loop will run
	message = input(prompt)

	if message == 'quit':
		print("Okay, we're done here.")
		active = False						# active turns False (and thus the while loop stops) when message == 'quit'
	else:
		print(message)

# this makes it easier to add more tests inside the while loop, instead of the != part of the previous example
# any of a number of conditions or tests could cause active to become False


print()


# use a BREAK statement to control the flow and execute only desired lines

prompt = "\nEnter the name of a city you have visited "
prompt += "\n(Enter quit when you are finished.) "

while True:					# this loop will run until something tells it to stop
	city = input(prompt)

	if city == 'quit':
		print("Okay, see you later")
		break				# this causes Python to exit the loop
	else:
		print(f"I'd love to go to {city}")

#  BREAK statements work in any Python loop, like FOR loops

print()


# can return to the beginning of a loop with a CONTINUE statement

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:	# in other words, if it's even
		continue				# if the number is even, it breaks out of the loop, thus bypassing the print() call
								# in this way, only odd numbers are printed
	print(current_number)



# Infinite loops

x = 1
while x <= 5:
	print(x)
	x += 1 		# if this is ommited, the loop would run forever

# Avoid by testing loops and making sure they do what you intend

