# 7-8 Deli

sandwich_orders = ['ruben', 'club', 'grilled cheese', 'blt']
finished_orders = []


while sandwich_orders:
	made_order = sandwich_orders.pop()
	print(f"Making a {made_order}")
	finished_orders.append(made_order)

print("\nThe following orders have been made:")
for order in finished_orders:
	print(order)

print()


# 7-9 No pastrami

sandwich_orders = ['ruben', 'pastrami', 'club', 'pastrami', 'grilled cheese', 'pastrami', 'blt']

print("Sorry, we are out of pastrami")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

print("Here is what we have:")
for sandwich in sandwich_orders:
	print(f"\t{sandwich}")


print()

# 7-10 Dream Vacation

vacations = {}

poll_active = True
while poll_active:
	name = input("\nWhat is your name? ")
	location = input("If you could visit one place in the world, where would you go? ")
	vacations[name] = location

	next_answer = input("Is there anyone else who needs to answer? (y/n) ")
	if next_answer == 'n':
		poll_active = False

for name, location in vacations.items():
	print(f"\n{name.title()} wants to go to {location.title()}.")

print("\nThose are some great ideas. Start traveling!")


# I initially put the 'next_answer' line after location and before 'if next_answer...'
#	this resulted in an error in the for loop at the end
# 	saying that 2 values were expected


