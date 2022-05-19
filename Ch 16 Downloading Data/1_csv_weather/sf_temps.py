import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sf_weather_2018.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	# for index, column_header in enumerate(header_row):
	# 	print(index, column_header)
			# 0 STATION
			# 1 NAME
			# 2 DATE
			# 3 PRCP
			# 4 TAVG
			# 5 TMAX
			# 6 TMIN

	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high = int(row[5])
			low = int(row[6])
		except ValueError:
			print(f"No data for {current_date}")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("Daily high and low temperatures in San Fransisco, CA, 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.ylim(20,130)

plt.show()