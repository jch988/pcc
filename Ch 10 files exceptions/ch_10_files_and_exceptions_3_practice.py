from new_section import new_section as ns

# 10-6 Addition & 10-7 Addition Calculator


# prompt = "Give me two numbers and I will add them together"
# prompt += "\nEnter 'q' to quit"

# while True:
# 	num_1 = input("First number: ")
# 	if num_1 == 'q':
# 		break
# 	num_2 = input("Second number: ")
# 	if num_2 == 'q':
# 		break
# 	try:
# 		answer = int(num_1) + int(num_2)
# 	except ValueError:
# 		print("Please enter only numbers")
# 	else:
# 		print(f"The answer is {answer}")



ns()

# 10-8, 10-9 Cats and Dogs

filenames = ['cats.txt', 'dogs.txt']

for file in filenames:
	try:
		with open(file) as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"'{file}' cannot be located")
		# pass
	else:
		print(f"{contents}\n")


ns()

# 10-10 Common Words

filenames = ['sunreach.txt', 'redawn.txt', 'evershore.txt']

# use .count() method
for book in filenames:
	with open(book) as b:
		contents = b.read()
		print(f"'the' appears in {book} {contents.count('the')} times")
# >>> 'the' appears in sunreach.txt 3512 times
# >>> 'the' appears in redawn.txt 4750 times
# >>> 'the' appears in evershore.txt 4719 times

ns()

# catch all the upper case words by using .lower() method on the contents
for book in filenames:
	with open(book) as b:
		contents = b.read()
		print(f"'the' appears in {book} {contents.lower().count('the')} times")
# >>> 'the' appears in sunreach.txt 3866 times
# >>> 'the' appears in redawn.txt 5387 times
# >>> 'the' appears in evershore.txt 5285 times

ns()

# remove words like 'there' and 'then' by putting a space
for book in filenames:
	with open(book) as b:
		contents = b.read()
		print(f"'the' appears in {book} {contents.lower().count('the ')} times")
# >>> 'the' appears in sunreach.txt 2491 times
# >>> 'the' appears in redawn.txt 3324 times
# >>> 'the' appears in evershore.txt 3314 times