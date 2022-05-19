# Write interactive programs

# use the INPUT() function to get information from the user
# use WHILE LOOPS to keep a program running as long as certain conditions are met


message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# sublime text apparently cannot run a program like this??
# use terminal
# cd
# ls
# if the directory has spaces (like python crash course folder), must put in ''
# just 'cd' backs the directory up by one
# use exit() to get out of runnning python and back to directory



# add a space after the prompt to separate it form the user's input

name = input("What is your name? ")
print(f"Hello {name}!")


# can write a prompt over several lines, then pass to a variable. Looks cleaner.

prompt = "If you tell us who you are, we can personalize messages you see."
prompt += "\nWhat is your name? "

name = input(prompt)
print(f"Hello {name}!")


# python interprets answers to input as STRINGS
# use int() to turn it into a number if needed

age = input("How old are you? ")
print(age)
# this returns a 'string'

age = input("How old are you? ")
age = int(age)
print(age)

# or

age = int(input("How old are you? "))
print(age)

# these both return integers


print()

height = input("How tall are you in inches? ")
height = int(height)

if height >= 48:
	print("\nYou're tall enough to ride!")
else:
	print("\nSorry, you'll be able to ride when you're older.")



print()


# The MODULO OPERATOR % divided one number by another and returns the REMAINDER
# use this to determine if a number is even or odd

# if num % 2 is zero, then it's even (there is no remainder..it divides clean)
# if num % 2 has a remainder, it must be odd

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
	print("That's an even number.")
else:
	print("That's an odd number.")






