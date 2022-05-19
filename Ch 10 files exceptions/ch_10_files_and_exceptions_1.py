from new_section import new_section as ns

# files - analyze a lot of data
# exceptions - special objects to manage errors
# json - save work and come back later

# Programs become more aplicable, usable, and stable


# 10.1
# Reading from a file

with open('pi_digits.txt') as file_object:
	contents = file_object.read()			# 'open' is only available in the 'with' block
print(contents)
# >>> 3.1415926535 
# >>>  8979323846 
# >>>  2643383279


# .read() returns empty string ('\n) at the end of the file
# use print(contents.rstrip()) to remove


# file in a folder in the same directory?
with open('downloads/chapter_10/pi_digits.txt') as file_object:
	contents = file_object.read()
print(contents)

 # in another directory altogther?

	# file_path = '/Users/JCH/pi_digits.txt'
	# with open(file_path) as file_object:
	# 	contents = file_object.read()
	# print(contents)



filename = 'pi_digits.txt'     # can swap this out later for other files if needed

# read file line by line

with open(filename) as file_object:
	for line in file_object:
		print(line)
# >>> 3.1415926535

# >>>  8979323846 

# >>>  2643383279




with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())	# remove '\n' form the end of each line
# >>> 3.1415926535 
# >>>  8979323846 
# >>>  2643383279


ns()


# work with the lines from file after 'wtih' block
# store lines, recall later

with open(filename) as file_object:
	lines = file_object.readlines()	# stores each line as an element in a list called 'lines'

print(lines)
# >>> ['3.1415926535 \n', '  8979323846 \n', '  2643383279\n']

for line in lines:
	print(line)
# >>> 3.1415926535 

# >>>   8979323846 

# >>>   2643383279




# can now work with file in any way we want

ns()

# build a single string containing all the digits in the file

pi_string = ''
for line in lines:
	pi_string += line.strip()		# removes all whitespace left and right

print(pi_string)
# >>> 3.141592653589793238462643383279
print(len(pi_string))
# >>> 32



# imports from a text file are read as strings

print(type(pi_string))
# >>> <class 'str'>

# want number? Convert:

pi_string = float(pi_string)
print(type(pi_string))
# >>> <class 'float'>

# (cannot use int since there is a decimal; integer is for whole numbers)


ns()


newfilename = 'pi_million_digits.txt'

with open(newfilename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()


def pi(num):
	"""Prints out pi to the input number of decimal places"""
	decimals = num + 2
	print(f"pi to {num} decimal places: {pi_string[:decimals]}")

pi(4)
# >>> 3.1415
pi(8)
# >>> 3.14159265


birthday = input("Enter your birthday in the format mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi")

# 120372
# >>> Your birthday appears in the first million digits of pi!
# 051488
# >>> Your birthday does not appear in the first million digits of pi

