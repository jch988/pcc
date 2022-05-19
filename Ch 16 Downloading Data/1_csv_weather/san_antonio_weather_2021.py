import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/san_antonio_weather_data_2021.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# for index, column_header in enumerate(header_row):
	# 	print(index, column_header)
			# 0 STATION
			# 1 NAME
			# 2 DATE
			# 3 PRCP
			# 4 SNOW
			# 5 SNWD
			# 6 TAVG
			# 7 TMAX
			# 8 TMIN
			# 9 WT01
			# 10 WT02
			# 11 WT03
			# 12 WT04
			# 13 WT06
			# 14 WT08

	# Get dates, high temps, and low temps from this file
	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[7])
		low = int(row[8])
		dates.append(current_date)
		highs.append(high)
		lows.append(low)

# Plot the high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha = 0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)

# Format plot
ax.set_title("Temperatures in San Antonio, Tx, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()