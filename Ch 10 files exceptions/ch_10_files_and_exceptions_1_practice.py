from new_section import new_section as ns

# 10-1 Learning Python

filename = 'learning_python.txt'

with open(filename) as file_object:
	contents = file_object.read()


print(contents)

ns()

with open(filename) as file_object:
	for line in file_object:
		print(line)

ns()


with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())


ns()

with open(filename) as file_object:
	lines_list = file_object.readlines()

print(lines_list)

for line in lines_list:
	print(line)

ns()

lines_string = ''
for line in lines_list:
	lines_string += line.strip() + " "
print(lines_string)

ns()

# 10-2 Learning C

lines_c = lines_string.replace('Python', 'C')
print(lines_c)

