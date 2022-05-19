import matplotlib.pyplot as plt

from random_walk import RandomWalk

print("Running simulation")

x_axis = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
y_axis = []
	
for num in x_axis:
	simulations = []
	while len(simulations) < 100:
		runs = 0
		while True:
			runs += 1
			rw = RandomWalk(num)
			rw.fill_walk()
			if rw.x_values[-1] and rw.y_values[-1] == 0:
				simulations.append(runs)
				break
	y_axis.append(runs)
	average_num_runs = sum(simulations) / len(simulations)
	print(f"After {len(simulations)} simulations of {num} steps each, it took {average_num_runs} runs on average to end up where we started")

plt.style.use('classic')
fix, ax = plt.subplots()
ax.scatter(x_axis, y_axis, s=20)

ax.set_title("Random walk simulation")
ax.set_xlabel("Number of steps in simulation")
ax.set_ylabel("Number of runs to return to start")

plt.show()


