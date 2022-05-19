import json

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
	all_eq_data = json.load(f)

# Explore the structure of the data
# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
# 	json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags = [x['properties']['mag'] for x in all_eq_dicts]
lons = [x['geometry']['coordinates'][0] for x in all_eq_dicts]
lats = [x['geometry']['coordinates'][1] for x in all_eq_dicts]

print(mags[:5])
print(lons[:5])
print(lats[:5])

