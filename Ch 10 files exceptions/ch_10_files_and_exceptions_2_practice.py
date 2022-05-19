from new_section import new_section as ns

# 10-3 Guest

# filename = 'ch_10_practice.txt'
# name = input("What is your name? ")
# with open(filename, 'a') as file_object:	
# 	file_object.write(f"{name}\n")

ns()

# 10-4 Guest Book

# guest_file = 'ch_10__practice_guest_book.txt'
# prompt = "Add your name to the guest book (enter 'q' if you are the last guest.) "
# active = True
# while active:
# 	name = input(prompt)
# 	if name == 'q':
# 		active = False
# 	else:
# 		with open(guest_file, 'a') as file_object:
# 			file_object.write(f"{name} was here. \n")


ns()

# 10-5 Programming Poll

prog_file = 'ch_10_practice_prog.txt'

prompt = "Why do you like programming? ('q' to quit) "

active = True
while active:
	answer = input(prompt)
	if answer == 'q':
		active = False
	else:
		with open(prog_file, 'a') as file_object:
			file_object.write(f"{answer}\n")
			