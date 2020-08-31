"""Level 3.3"""


def solution(x, y):
	generations = 0
	x, y = int(x), int(y)
	if x > y:
		x, y = y, x
	while x > 1:
		generations += y // x
		x, y = y % x, x
		if x == 0:
			return "impossible"
	return str(generations + y - 1)
