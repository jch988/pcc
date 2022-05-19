guest_list = ['Theodore Roosevelt', 'Joe Rogan', 'Margery']
print(guest_list)
print()
print(f"Hey {guest_list[0]}, would you like to come to dinner at my house tonight? I would like to hear the 'Man in the Arena' speech in person!")
print(f"Hey {guest_list[1]}, would you like to come to dinner at my house tonight? We can have a long conversation!")
print(f"Hey {guest_list[2]}, would you like to come to dinner at my house tonight? You can tell me all about your new religious beliefs!")


# print the number of people invited using len()
print(f"\nLooks like there are {len(guest_list)} people invited")

print(f"\nIt looks like {guest_list.pop()} can't make it since she was blown up. Here is the revised guest list:")
print(guest_list)


print("\nYou know what, I'll invite Cersei instead. Here is the new list:")
guest_list.append('Cersei Lannister')
print(guest_list)
print(f"{guest_list[-1]} is the new addition!")


print("\nIt turns out I have found a bigger table. Here is the new list:")
guest_list.insert(0, 'Walter White')
guest_list.insert(2, 'Mattie Rogers')
guest_list.append('Mat Fraser')

print(f"\nThere are now {len(guest_list)} people invited:")
print(guest_list)

print(f"\nHey {guest_list[0]}, would you like to come to dinner at my house tonight? Don't worry, I'll do the cooking.")
print(f"Hey {guest_list[2]}, would you like to come to dinner at my house tonight? I'll make sure you are in a calorie surplus.")
print(f"Hey {guest_list[4]}, would you like to come to dinner at my house tonight? I know you don't have any kids to take care of.")
print()
print("Well, it looks like my new table will not arrive in time, and now I only have space for two guests.")
print()
print(f"Sorry {guest_list.pop(-2)}, you're kind of a bitch anyway, so don't come over")
print(f"Hey {guest_list.pop()}, I know you don't like making public appearances, so don't worry about it—stay home.")
print (f"{guest_list.pop(2)}, you need to work on that clean and jerk, so get in the gym instead!")
print(f"Finally, {guest_list.pop(0)}, you are not going to be the one who knocks (on my front door) this time.")
print()
print(f"Ok y'all. Looks like its down to {guest_list}")
print("Nevermind, I don't want anyone over tonight")
del guest_list[1]
del guest_list[0]
print(guest_list)
