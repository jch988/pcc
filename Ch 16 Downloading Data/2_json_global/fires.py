import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/fires_us.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	# print(header_row)

	# for index, column_header in enumerate(header_row):
	# 	print(index, column_header)

		# 0 latitude
		# 1 longitude
		# 2 brightness
		# 3 scan
		# 4 track
		# 5 acq_date
		# 6 acq_time
		# 7 satellite
		# 8 confidence
		# 9 version
		# 10 bright_t31
		# 11 frp
		# 12 daynight

	lats, longs, intensity = [], [], []
	for row in reader:
		latitude = float(row[0])
		longitude = float(row[1])
		brightness = float(row[2])
		lats.append(latitude)
		longs.append(longitude)
		intensity.append(brightness)
 
data = [{
 	'type': 'scattergeo',
 	'lon': longs,
 	'lat': lats,
 	'marker':{
 		# 'size': [1.1*intense for intense in intensity],
 		'color': intensity,
 		'colorscale': 'Hot',
 		'reversescale': True,
 		'colorbar': {'title': 'Brightness'},
 	}
 }]

my_layout = Layout(title='US Fires Past 24 hours')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='us_fires.html')