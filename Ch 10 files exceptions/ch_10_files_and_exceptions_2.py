from new_section import new_section as ns

filename = 'downloads/chapter_10/programming.txt'	# If this doesn't exit, Python will create it


with open(filename, 'w') as file_object:			
	file_object.write("I love programming.")
# >>> I love programming.


# w = open the file in 'write' mode (erases contents if the file already exists)
# r = read mode
# a = append mode
# r+ = read and write
# no argument = opens in read-only mode by default


# doing this multiple times doesn't add new lines.

with open(filename, 'w') as file_object:			
	file_object.write("I love programming.")
	file_object.write("I love creating new games.")
# >>> I love programming.I love creating new games.

# must put the new lines in

with open(filename, 'w') as file_object:			
	file_object.write("I love programming.\n") 
	file_object.write("I love creating new games.\n")
# >>> I love programming.
# >>> I love creating new games.


# use append mode to add to the file

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser. \n")
