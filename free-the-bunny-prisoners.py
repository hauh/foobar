"""Level 4.1"""


def shift(positions, lenght):
	for i in reversed(range(len(positions))):
		if positions[i] < i + lenght - len(positions):
			positions[i] += 1
			for j in range(i + 1, len(positions)):
				positions[j] = positions[j - 1] + 1
			return True
	return False


def solution(num_buns, num_required):
	positions = list(range(num_buns - num_required + 1))
	keys = [[] for _ in range(num_buns)]
	key_number = 0
	while True:
		for i in positions:
			keys[i].append(key_number)
		if not shift(positions, num_buns):
			break
		key_number += 1
	return keys
