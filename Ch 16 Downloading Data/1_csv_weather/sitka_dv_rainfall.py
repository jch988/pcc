import csv
from datetime import datetime
import matplotlib.pyplot as plt

sitka_file = 'data/sitka_weather_2018_simple.csv'
dv_file = 'data/death_valley_2018_simple.csv'

with open(sitka_file) as f:
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
	sitka_dates, sitka_precipitation = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			rainfall = float(row[3])
		except ValueError:
			print(f"No data for {current_date}")
		else:
			sitka_dates.append(current_date)
			sitka_precipitation.append(rainfall)


with open(dv_file) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	# for index, column_header in enumerate(header_row):
	# 	print(index, column_header)
			# 0 STATION
			# 1 NAME
			# 2 DATE
			# 3 PRCP
			# 4 TMAX
			# 5 TMIN
			# 6 TOBS
	dv_dates, dv_precipitation = [], []
	for row in reader:
		rainfall = float(row[3])
		dv_precipitation.append(rainfall)
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			rainfall = float(row[3])
		except ValueError:
			print(f"No data for {current_date}")
		else:
			dv_dates.append(current_date)
			dv_precipitation.append(rainfall)







plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dv_dates, sitka_precipitation, c='blue')
ax.plot(dv_dates, dv_precipitation, c='red')

ax.set_title("Daily precipitation levels in Sitka, AK and Death Valley, CA, 2018")
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation (in)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
