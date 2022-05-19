import json

filename = 'ch_10_numbers.json'
with open(filename) as f:
	numbers = json.load(f)

print(numbers)