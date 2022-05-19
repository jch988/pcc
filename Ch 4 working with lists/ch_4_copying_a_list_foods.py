my_foods = ['pizza', 'falafel', 'okra']
friend_foods = my_foods[:]
# the [:] copies the list
# anything further added to either list is added only to THAT particular list

my_foods.append('canoli')
# only added to my_foods

friend_foods.append('ice cream')
# only added to friend_foods

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

