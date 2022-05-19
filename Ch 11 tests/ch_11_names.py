from ch_11_testing_1 import get_formatted_name_2

print("Enter 'q' at any time to quit")
while True:
	first = input("What is your first name? ")
	if first == 'q':
		break
	last = input("What is your last name? ")
	if last == 'q':
		break

	formatted_name = get_formatted_name_2(first, last)
	print(f"\tYour name is {formateed_name}")
