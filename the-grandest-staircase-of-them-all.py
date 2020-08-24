"""Level 3.1"""

saved = {}


def build(height, bricks):
	ladders = 0
	for next_height in range(1, height):
		bricks_left = bricks - next_height
		if not bricks_left:
			return ladders + 1
		next_ladders = saved.get((next_height, bricks_left))
		if next_ladders is None:
			next_ladders = build(next_height, bricks_left)
			saved[(next_height, bricks_left)] = next_ladders
		ladders += next_ladders
	return ladders


def solution(n):
	ladders = 0
	for height in range(2, n):
		ladders += build(height, n - height)
	return ladders
