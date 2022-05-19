
# 4-10 slices
# using one of the programs fron this ch, add several lines to the end that do the following:
#  	print "The first three items on this list are:"
# 	print "The items from the middle of the list are:"
# 	print "The last three items are:"
# 	and print the slice of each accordingly

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(f"The first three items on this list are: {players[0:3]}")
print(f"The items fom the middle of the list are: {players[1:4]}")
print(f"The last three items on this list are: {players[-3:]}")

print()

# 4-11 use the program from 4-1 (pizzas)
# Make a copy of the list, call it friend_pizza, then:
# 	Add a new pizza to the original list
# 	Add a new pizza to the friend's list
# 	Prove that you have two separate lists


my_pizzas = ['supreme', 'pineapple', 'pesto']
friend_pizzas = my_pizzas[:]

my_pizzas.append('cheese')
friend_pizzas.append('deep dish')
friend_pizzas.remove('pineapple')

print(my_pizzas)
print(friend_pizzas)

for pizza in my_pizzas:
	print(f"I like {pizza} pizza.")

for pizza in friend_pizzas:
	print(f"My friend likes {pizza} pizzas")


# 4-13 Tuples
# think of five foods and store them in a tuple
# use a for-loop to print the menu items
# try to modify one of them, make sure the change is rejected
# Add a line that rewrites the entire menu, since two of the items have changed

menu = 'bagels', 'sandwiches', 'sweet potatoes', 'yogurt', 'eggs'
print(f"\nThe menu contains:")
for food in menu:
	print(food)

# menu[0] = 'cheese'

new_menu = 'cheese', 'sandwiches', 'sweet potatoes', 'steak', 'eggs'
print(f"\nThe new menu contains:")
for food in new_menu:
	print(food)
