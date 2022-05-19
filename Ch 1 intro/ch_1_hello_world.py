message = "Hello Python Crash Course readers"
print (message)

message = "Hello to you, too"
print(message)



nums = list(range(1,11))
my_list = []
for n in nums:
	if n%2 == 0:
		my_list.append(n)
print(my_list)


my_list = [n for n in nums if n%2 == 0]
print(my_list)