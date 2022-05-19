def make_pizzas(size, *toppings):
	"""Summarize the pizza to be made"""
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"\t-{topping}")


def greet_user(username):			
	"""Display a simple greeting"""
	print(f"Hello {username.title()}!")


def fun1():
	print("Called by fun1")

def fun2():
	print("Called by fun2")
	fun1()