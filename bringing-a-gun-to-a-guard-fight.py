"""Level 4.2"""


def solution(dimensions, your_pos, guard_pos, distance):
	distance_squared = distance ** 2

	def in_range(x, y):
		return (your_pos[0] - x) ** 2 + (your_pos[1] - y) ** 2 <= distance_squared

	if not in_range(*guard_pos):
		return 0

	your_mirrors = []
	guard_mirrors = []
	start_pos = []
	shots = 0

	for i in (0, 1):
		your_coords = [-your_pos[i], your_pos[i]]
		guard_coords = [-guard_pos[i], guard_pos[i]]

		start = -dimensions[i]
		while start > -distance:
			your_coords.insert(0, your_coords[1] - dimensions[i] * 2)
			guard_coords.insert(0, guard_coords[1] - dimensions[i] * 2)
			start -= dimensions[i]

		start = dimensions[i]
		while start < distance + dimensions[i]:
			your_coords.append(your_coords[-2] + dimensions[i] * 2)
			guard_coords.append(guard_coords[-2] + dimensions[i] * 2)
			start += dimensions[i]

		start = your_coords.index(your_pos[i])
		start_coords = [start] * 2
		if your_pos[i] >= guard_pos[i]:
			start_coords[0] += 1
		if your_pos[i] <= guard_pos[i]:
			start_coords[1] -= 1
		if your_pos[i] == guard_pos[i]:
			shots = 1

		your_mirrors.append(your_coords)
		guard_mirrors.append(guard_coords)
		start_pos.append(start_coords)

	def get_angle(x, y):
		try:
			return float(y - your_pos[1]) / (x - your_pos[0])
		except ZeroDivisionError:
			return float('Inf')

	def check_mirrored_room(ix, iy, closed_angles):
		x = guard_mirrors[0][ix]
		y = guard_mirrors[1][iy]
		closed_angles.add(get_angle(your_mirrors[0][ix], your_mirrors[1][iy]))
		angle = get_angle(x, y)
		if angle in closed_angles or not in_range(x, y):
			return False
		closed_angles.add(angle)
		return True

	def check_quadrant(start, direction_x, direction_y):
		ix = start[0]
		iy = start[1]
		if (ix < 0 or ix == len(guard_mirrors[0])
		or iy < 0 or iy == len(guard_mirrors[1])):
			return
		closed_angles = set()
		directions = [direction_x, direction_y]

		while not (direction_x == direction_y == 0):
			if ix in (0, len(guard_mirrors[0]) - 1):
				direction_x = 0
			if iy in (0, len(guard_mirrors[1]) - 1):
				direction_y = 0

			shots = 0
			for x in range(start[0], ix, directions[0]):
				shots += check_mirrored_room(x, iy, closed_angles)
			for y in range(start[1], iy, directions[1]):
				shots += check_mirrored_room(ix, y, closed_angles)
			shots += check_mirrored_room(ix, iy, closed_angles)

			ix += direction_x
			iy += direction_y
			yield shots

	quadrants = []
	quadrants.append(check_quadrant((start_pos[0][0], start_pos[1][0]), 1, 1))
	quadrants.append(check_quadrant((start_pos[0][1], start_pos[1][0]), -1, 1))
	quadrants.append(check_quadrant((start_pos[0][1], start_pos[1][1]), -1, -1))
	quadrants.append(check_quadrant((start_pos[0][0], start_pos[1][1]), 1, -1))

	while any(quadrants):
		for index, check in enumerate(quadrants):
			if check:
				try:
					shots += next(check)
				except StopIteration:
					quadrants[index] = None

	return shots
