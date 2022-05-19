
for value in range(1, 5):
	print(value)
# starts counting at the first value given, stops at the second, but does not include the second

numbers = list(range(1,6))
print(f"Numbers 1-5: {numbers}")
# stops at 6 (but does not include 6), so up to 5 is in the list

even_numbers = list(range(2, 11, 2))
print(f"Even numbers: {even_numbers}")
# starts at 2, stops at 11 (so 10, really), goes up by 2 each time

odd_numbers = list(range(1,11,2))
print(f"Odd numbers: {odd_numbers}")
# starts at 1, stops at 11, goes up by 2 each time

square_numbers = []
for value in range(1,9):
	squares = value**2
	square_numbers.append(squares)
print(f"Here are squares of one to eight: {square_numbers}")
# 1) start with empty list
# 2) loops through each value in 1-10 with range() function
# 3) each value (1, 2, 3, etc) gets squared and added to 'squares'
# 4) each new 'squares' results is appended to the list 'square_numbers'

square_numbers = []
for value in range(1,10):
	square_numbers.append(value**2)
print(f"Here are squares of one to nine: {square_numbers}")
# same as before, but omits one line
# now, 'square numbers' is directly appended with a value that is squared from the range

# Focus first on writing code that you understand clearly, then look for more efficient approaches

squares = [value**2 for value in range(1,11)]
print(f"Here are squares of one to ten: {squares}")
# List Comprehensions combine the 'for' loop and the creation of new elements into one line
# 

