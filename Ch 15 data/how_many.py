from random_walk import RandomWalk

print("Running simulation")

simulations = []
num_steps = 1_000
while len(simulations) < 10:
	runs = 0
	while True:
		runs += 1
		rw = RandomWalk(num_steps)
		rw.fill_walk()
		if rw.x_values[-1] and rw.y_values[-1] == 0:
			simulations.append(runs)
			break
	print(f"It took {runs} runs until we ended up where we started.")

average_num_runs = sum(simulations) / len(simulations)

print(f"After {len(simulations)} simulations of {num_steps} steps each, it took {average_num_runs} runs on average to end up where we started")
print(f"Lowest number of runs: {sorted(simulations)[0]}")
print(f"Highest number of runs: {sorted(simulations)[-1]}")



