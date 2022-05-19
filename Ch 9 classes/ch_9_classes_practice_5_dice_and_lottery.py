from new_section import new_section as ns

# 9-13 Dice

from random import randint

class Die:

	def __init__(self, sides):
		self.sides = sides

	def roll_die(self):
		# print(f"Rolling a {self.sides}-sided die:")
		return randint(1, self.sides)


new_game = Die(6)
print(f"Rolling a {new_game.sides}-sided die:")
rolls = 1
while rolls <= 10:
	print(f"Roll number {rolls} is {new_game.roll_die()}")
	rolls += 1

ns()

next_game = Die(10)
print(f"Rolling a {next_game.sides}-sided die:")
rolls = 1
while rolls <= 10:
	print(f"Roll number {rolls} is {next_game.roll_die()}")
	rolls += 1

ns()

another_game = Die(20)
print(f"Rolling a {another_game.sides}-sided die:")
rolls = 1
while rolls <= 10:
	print(f"Roll number {rolls} is {another_game.roll_die()}")
	rolls += 1

ns()

# 9-14 Lottery

from random import choice

lottery = [4, 8, 15, 16, 23, 42, 5, 14, 88, 22, 'l', 'e', 't', 'r', 's' ]
winners = []
my_ticket = []

def get_winners():
	"""select 4 random numbers and adds them to the list 'winners'"""
	# winners = []
	selections = 0
	while selections < 4:
		selection = choice(lottery)
		winners.append(selection)
		selections += 1
	print (f"Any ticket with {winners} has won!")
	# return winners

def make_my_ticket():
	selections = 0
	while selections < 4:
		selection = choice(lottery)
		my_ticket.append(selection)
		selections += 1
	print(my_ticket)
	# return my_ticket

make_my_ticket()

attempts = 1
while my_ticket != winners:
	winners = []
	get_winners()
	attempts += 1
else:
	if attempts == 1:
		print(f"It took {attempts} try for my ticket to win")
	elif attempts > 1:
		print(f"It took {attempts} tries for my ticket to win")
