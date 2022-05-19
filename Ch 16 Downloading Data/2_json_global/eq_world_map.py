import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_past_hour.json'
with open(filename) as f:
	all_eq_data = json.load(f)

# Explore the structure of the data
# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
# 	json.dump(all_eq_data, f, indent=4)

# Create list of all earthquake dictionary
# all_eq_dicts = all_eq_data['features']

# Take out relevant data from each earthquake dictionary
mags = [x['properties']['mag'] for x in all_eq_data['features']]
lons = [x['geometry']['coordinates'][0] for x in all_eq_data['features']]
lats = [x['geometry']['coordinates'][1] for x in all_eq_data['features']]
hover_texts = [x['properties']['title'] for x in all_eq_data['features']]
chart_title = all_eq_data['metadata']['title']

# Map the earthquakes
data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,
	'text': hover_texts,
	'marker': {
		'size': [5*mag for mag in mags],
		'color': mags,
		'colorscale': 'Hot',
		'reversescale': True,
		'colorbar': {'title': 'Magnitude'},
	}
}]

my_layout = Layout(title=chart_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')