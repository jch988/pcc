# Functions modifying values: variables, lists, and dictionaries
# https://www.dataquest.io/blog/tutorial-functions-modify-lists-dictionaries-python/

num_1 = 5
num_2 = 10

def multiply_and_add(num_1, num_2):
	num_1 = num_1 * 10	# 50
	num_2 = num_2 * 10	# 100
	return num_1 + num_2	# 150

a_sum = multiply_and_add(num_1, num_2)	#150

print(a_sum)	# 150, from function
print(num_1)	# original num_1
print(num_2)	# original num_2

print("---------------------")

initial_list = [1, 2, 3]

def duplicate_last(a_list):
	"""Duplicates the final entry in the data"""
	last_element = a_list[-1]
	a_list.append(last_element)
	return a_list

print(f"Initial list BEFORE function call: {initial_list}")

new_list = duplicate_last(a_list = initial_list[:])

print(f"Initial list AFTER function call: {initial_list}")
print(f"New list: {new_list}")

print("---------------------")

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622,}

def make_percentages(a_dictionary):
	"""figure out what percentage of apps fall into each age rating"""
	total = 0 					#total number of apps

	#loop through a_dictionary to count the number of apps
	for key in a_dictionary:
		count = a_dictionary[key]
		total += count				# loops through each key and adds it to total

	# loop through a_dictionary again
	for key in a_dictionary:
		a_dictionary[key] = (a_dictionary[key] / total) * 100

	return a_dictionary

print(f"content_ratings BEFORE function call: {content_ratings}")

ratings_percentages = make_percentages(content_ratings)

print(f"content_ratings AFTER function call: {content_ratings}")

print(f"Ratings percentages: {ratings_percentages}")




# Lists and Dictionaries are MUTABLE
# Changing them inside the function changes them overall



print("---------")

number = 5

def multiply(number):
	number = number * 10
	return number

new_number = multiply(number)
print(f"Number: {number}")
print(f"New number: {new_number}")



print("-----------")

first_list = [1, 2, 3]

def change_list(first_list):
	list_copy = first_list.copy()
	list_copy.append(4)
	return list_copy

print(f"first_list BEFORE function call {first_list}")
new_list = change_list(first_list)
print(f"first_list AFTER function call: {first_list}")
print(f"new_list: {new_list}")