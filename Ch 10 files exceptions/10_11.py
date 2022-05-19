import json

filename = 'ch_10_fav_num.json'
with open(filename) as f:
	answer = json.load(f)
print(answer)