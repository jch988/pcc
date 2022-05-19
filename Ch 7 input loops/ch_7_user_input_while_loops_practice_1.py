# 7-1 Rental car

car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find a {car.title()}.")


print()

# 7-2 Restaurant seating


group = input("How many are in your dining group? ")
group = int(group)

if group > 8:
	print("There will be a brief wait, is that okay?")
else:
	print("We have a table ready.")

print()

# 7-3 Mupltiples of ten

number = input("Give me a number ")
number = int(number)

if number % 10 == 0:
	print("That IS a multiple of ten.")
else:
	print("NOT a multiple of ten.")
























