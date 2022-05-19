cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list in alphabetical order, and reverse:")
print(sorted(cars))
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)


print()
cars.reverse()
print("Here is the output with 'cars.reverse'. This reversees the original order of the list:")
print(cars)
