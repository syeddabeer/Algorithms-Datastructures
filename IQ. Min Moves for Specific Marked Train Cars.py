# /***
# moving specific marked train cars identified by letters from different tracks to another in multiples of three, while also moving the ones that weren't marked out of the way.
# ***/

def min_moves_multi(track, marked_cars, group_size):
	marked_set = set(marked_cars)
	results = {}
	for car_type in marked_set:
		positions = [i for i, c in enumerate(track) if c == car_type]
		moves = 0
		for g in range(0, len(positions), group_size):
			group = positions[g:g+group_size]
			if len(group) < group_size:
				break 
			first, last = group[0], group[-1]
			span = track[first : last+1]
			blockers = sum(1 for c in span if c!=car_type)
			moves += blockers
		results[car_type] = moves # 'T': 3, 'H': 5
	total = sum(results.values())
	return total, results

def min_moves_multi_track(tracks, marked_cars, group_size):
	all_results = {}
	grand_total = 0

	for track_name, track in tracks.items(): # j : 1, k:2 
		total, results = min_moves_multi(track, marked_cars, group_size)
		all_results[track_name] = results 
		grand_total += total 
	return grand_total, all_results




# Example
# ── Example ──────────────────────────────────────────────────────
tracks = {
    'A' : ['A', 'T', 'X', 'B', 'T', 'X', 'T', 'Z', 'C', 'X'],
    'B' : ['T', 'Z', 'T', 'D', 'T', 'Z', 'E', 'Z', 'X', 'T'],
    'C' : ['X', 'X', 'A', 'X', 'T', 'Z', 'T', 'Z', 'T', 'Z'],
}
marked_cars = ['T', 'X', 'Z']


