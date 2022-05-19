# Lists that cannot change are 'immutable'
# Python calls immutable lists 'Tuples'

# Tuples use () instead of []

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250
#  if you try to do this, there is a 'TypeError' saying that "'Tuple' object does not support item assignment"

# Technically, a tuple just needs a comma; the () makes it look neater, but Python is fine if they aren't present:
my_t = 3,0
print(f"No comma: {my_t}")

# for loops work, too
for dimension in dimensions:
	print(dimension)

# Tuples can't be changed, but they can be redefined
print("\nOriginal dimensions:")
for dimension in dimensions:
	print(dimension)
dimensions = 400,100
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)





