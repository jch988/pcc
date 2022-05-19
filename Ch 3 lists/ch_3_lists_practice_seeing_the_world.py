# places I'd like to visit
places = ['peru', 'vietnam', 'japan', 'yellowstone', 'scotland', 'austria', 'sagamore hill']

# print original list
print("Here is the original list:")
print(places)

# use sorted() to print list in alphabetical order without modifying the actual list
print("\nHere is the list in APLABETICAL order:")
print(sorted(places))

# print the original list to show that it is still in order
print("\nHere is the original list again:")
print(places)

# use sorted() to print the list in reverse alphabetical order without modifying the actual list
print("\nHere is the list in REVERSE ALPHABETICAL order:")
print(sorted(places, reverse=True))

# print the original list to show that it is still in order
print("\nHere is the original list again:")
print(places)

# use reverse() to change the order of the list. Print the list to show that it's order has changed
places.reverse()
print("\nHere is the list in REVERSE order:")
print(places)

# use reverse() to change the order again. Print to show the original list.
places.reverse()
print("\nHere it is back in the original order again:")
print(places)

# use sort() to change the list so it's stored in alaphabetical order. Print it.
places.sort()
print("\nThe order of places has now been PERMANENTLY changed to alphabetical order:")
print(places)

# use sort() so the list is stored in reverse alphabetical order. Print it.
places.sort(reverse=True)
print("\nNow it is stored in REVERSE alphabetical order:")
print(places)

