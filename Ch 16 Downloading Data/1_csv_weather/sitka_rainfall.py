import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
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

	dates, precipitation = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			rainfall = float(row[3])
		except ValueError:
			print(f"No data for {current_date}")
		else:
			dates.append(current_date)
			precipitation.append(rainfall)

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, precipitation, c='blue')

ax.set_title("Daily precipitation levels in Sitka, AK, 2018")
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation (in)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
