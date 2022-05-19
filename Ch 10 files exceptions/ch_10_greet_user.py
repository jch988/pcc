import json

filename = 'ch_10_username.json'

with open(filename) as f:
	username = json.load(f)
	print(f"Welcome back, {username}")