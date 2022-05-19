# 8-3 T-shirt

def make_shirt(size, message):
	print(f"The shirt size is {size} and will say '{message}'")

# positional
make_shirt('medium', 'The Incredible Holt')
make_shirt('large', 'I am big')
print()

# keyword
make_shirt(message='The Incredible Holt', size='medium')
make_shirt(size='large', message='I am big')
print()


# 8-4 Large shirts

def make_shirt(message, size='large'):
	print(f"The shirt size is {size} and will say '{message}'")

make_shirt('I love Python')
make_shirt('I love tacos', size='medium')
make_shirt('I love nothing', size='small')


print()


# 8-5 Cities

def describe_city(name, country):
	print(f"{name} is in {country}.")

describe_city('San Antonio', 'The United States')

def describe_city(name, country='The United States'):
	print(f"{name} is in {country}.")

describe_city('Chicago')
describe_city('Columbus')
describe_city('Glasgow', country='Scotland')
describe_city('St. Louis')


