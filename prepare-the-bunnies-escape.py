"""Level 3.2"""

from collections import deque


def bfs(mp, height, width, best_lenght):
	q = deque(((0, 0, 1),))
	mp[0][0] = -1
	try:
		while q:
			y, x, lenght = q.pop()
			if lenght >= best_lenght:
				return best_lenght
			if y == height - 1 and x == width - 1:
				return lenght
			for a, b in ((1, 0), (0, 1), (-1, 0), (0, -1)):
				if (height > y + a >= 0) and (width > x + b >= 0) and mp[y + a][x + b] == 0:
					q.appendleft((y + a, x + b, lenght + 1))
					mp[y + a][x + b] = -1
		return best_lenght
	finally:
		for y in range(height):
			for x in range(width):
				if mp[y][x] == -1:
					mp[y][x] = 0


def is_blocked(mp, y, x, height, width):
	passages = 0
	for a, b in ((1, 0), (0, 1), (-1, 0), (0, -1)):
		if (height > y + a >= 0) and (width > x + b >= 0) and mp[y + a][x + b] == 0:
			passages += 1
			if passages == 2:
				return False
	return True


def solution(mp):
	height = len(mp)
	width = len(mp[0])
	best_lenght = bfs(mp, height, width, width * height)
	best_possible = width + height - 1
	if best_lenght == best_possible:
		return best_possible
	for y in range(height):
		for x in range(width):
			if mp[y][x] == 0 or is_blocked(mp, y, x, height, width):
				continue
			mp[y][x] = 0
			path = bfs(mp, height, width, best_lenght)
			if path < best_lenght:
				best_lenght = path
			mp[y][x] = 1
	return best_lenght
