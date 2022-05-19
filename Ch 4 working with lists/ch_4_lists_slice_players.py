
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# take a 'slice' of the list with [#:#]
# remember: indexes start at 0 and stop at—but do not include—the last number

print("Here are the first three players on my team:")
for name in players[0:3]:
	print(name.title())
# can write [0:3] or just [:3]. Result is the same

for name in players[:3]:
	print(f"Hey {name.title()}, you're in the game!")


for name in players[3:]:
	print(f"{name.title()}, you're up next!")
# [3:] starts at 3 and goes to the end


# can also slice the final entires on a long list
for name in players[-1:]:
	print(f"{name.title()}, You're the last one")


# if you don't include the :, it changes
for name in players[-1]:
	print(f"{name}, you're the last one")
# in this case it returns the last value on the list and applies the for loop to each letter


