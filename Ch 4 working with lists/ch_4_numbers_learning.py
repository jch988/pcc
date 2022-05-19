#4-3
for numbers in range (1, 21):
	print(numbers)

#4-4
#for num in range(1, 1_000_001):
#	print(num)

#4-5
print()
one_million = range(1,1_000_001)
print(min(one_million))
print(max(one_million))
print(sum(one_million))

#4-6
print()
nums = list(range(1, 21, 2))
print(nums)
for value in nums:
	print(value)

# 4-7
print()
threes = list(range(3, 31, 3))
print(threes)
for values in threes:
	print(values)


# 4-8
# cubes 1-10. Use FOR loop to print value of each.
print()

cubes_1_10 = []
for value in range (1,11):
	cube = value**3
	cubes_1_10.append(cube)
print(f"Cubes of one to ten: {cubes_1_10}")

cubes_1_11 = []
for value in range(1,12):
	cubes_1_11.append(value**3)
print(f"Cubes of one to eleven: {cubes_1_11}")

# 4-9

cubes_1_12 = [num**3 for num in range (1,13)]
print(f"Cubes of one to twelve: {cubes_1_12}")





