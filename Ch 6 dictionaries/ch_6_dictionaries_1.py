# Dictionaries allow you to connect pieces of related information
# can access and modify

# WORKING WITH DICTIONARIES

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# alien_0 is a dictionary that stores the color and point value

print()


# DICTIONARY - a collection of 'key-value' pairs
# above, key = 'color' and value = 'green'
# a key's value can be a number, string, list, or even another dictionary
# use {} around the entire dictionary, a : between key and value, and a comma b/t key-value pairs


new_points= alien_0['points']
print(f"You just earned {new_points} points!")

print()


# can add new key-value pairs at any time
# do this with dictionary_name['key'] = 'value'

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


print()

# it's sometimes necessary to start with an empty dictionary and add to it

alien_0 = {}
print(alien_0)
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print()

# values can be modified

print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}!")

print()

# example: tracking the position of an alien that can move at different speeds

alien_0 ={'color': 'green', 'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(alien_0)
print(f"Original x position: {alien_0['x_position']}")
print(f"This alien is {alien_0['speed']} speed")

# see how far to move
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

# calculate the new position
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x position: {alien_0['x_position']}.")


# changing only the 'speed': '_____' value in the first line will change the answer

print()

# the color is irrelevant here, so remove it

del alien_0['color']
print(alien_0)

# need only to enter the key to do this
# this is permanent

print()

# store one kind of information about many objects

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")
print(favorite_languages['sarah'])

print()


# print(alien_0['points']) shows error b/c 'points' key doesn't exist
# use get() method to set a value that will be returned if a key doesn't exist

point_value = alien_0.get('points', 'No point value assigned')
print(point_value)


