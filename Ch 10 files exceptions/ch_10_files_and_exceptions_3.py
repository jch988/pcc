from new_section import new_section as ns

# Exceptions
# 	- errors

# try-except block

# print(5/0)
# >>> ZeroDivisionError: division by zero

try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")
# >>> You can't divide by zero!



print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("\nSecond number: ")
	if second_number == 'q':
		break
	answer = int(first_number) / int(second_number)
	print(f"answer: {answer}")
# >>> if Second number is 0:
# >>> Traceback (most recent call last):
# >>>   File "/Users/JCH/Python/python crash course/ch_10_files_and_exceptions_3.py", line 29, in <module>
# >>>     answer = int(first_number) / int(second_number)
# >>> ZeroDivisionError: division by zero


while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("\nSecond number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by zero!")
	except ValueError:							# added this myself in case a letter is entered
		print("Please enter only a number")	
	else:								
		print(f"answer: {answer}")


ns()

# missing files...

filename = 'alice.txt'
# with open(filename) as f:
# 	contents = f.read()

# Traceback (most recent call last):
#   File "/Users/JCH/Python/python crash course/ch_10_files_and_exceptions_3.py", line 61, in <module>
#     with open(filename) as f:
# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'

try:
	with open(filename) as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file '{filename}' does not exist")
# >>> Sorry, the file 'alice.txt' does not exist


file = 'downloads/chapter_10/alice.txt'
try:
	with open(file) as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file '{file}' does not exist")
else:
	words = contents.split()	#creates a list containing each word; .split() separates by space
	num_words = len(words)
	print(f"This file has about {num_words} words")
# >>> This file has about 29465 words


ns()

# Analyze multiple files

# put code in a function, then write a FOR loop

def count_words(filename):
	"""Count the approximate number of words in a file"""
	try:
		with open(filename) as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Sorry, the file '{filename}' does not exist")
	else:
		words = contents.split()	#creates a list containing each word; .split() separates by space
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words")

filename = 'downloads/chapter_10/alice.txt'
count_words(filename)
# >>> This file has about 29465 words

ns()

filenames = ['downloads/chapter_10/alice.txt', 'downloads/chapter_10/little_women.txt', 
'downloads/chapter_10/siddhartha.txt', 'downloads/chapter_10/it.txt', 
'downloads/chapter_10/moby_dick.txt']

for filename in filenames:
	count_words(filename)

# >>> The file downloads/chapter_10/alice.txt has about 29465 words
# >>> The file downloads/chapter_10/little_women.txt has about 189079 words
# >>> The file downloads/chapter_10/siddhartha.txt has about 42172 words
# >>> Sorry, the file 'downloads/chapter_10/it.txt' does not exist
# >>> The file downloads/chapter_10/moby_dick.txt has about 215830 words


ns()

# Failing silently

# sometimes you don't want to report an exception

def count_words_again(filename):
	"""Count the approximate number of words in a file"""
	try:
		with open(filename) as f:
			contents = f.read()
	except FileNotFoundError:
		pass
	else:
		words = contents.split()	#creates a list containing each word; .split() separates by space
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words")

filenames = ['downloads/chapter_10/alice.txt', 'downloads/chapter_10/little_women.txt', 
'downloads/chapter_10/siddhartha.txt', 'downloads/chapter_10/it.txt', 
'downloads/chapter_10/moby_dick.txt']

for filename in filenames:
	count_words_again(filename)

# >>> The file downloads/chapter_10/alice.txt has about 29465 words
# >>> The file downloads/chapter_10/little_women.txt has about 189079 words
# >>> The file downloads/chapter_10/siddhartha.txt has about 42172 words
# >>> The file downloads/chapter_10/moby_dick.txt has about 215830 words

# The exception for IT no longer appears. SILENT!!
# Can do other things in the except block, like add the file name to a list of missing files

