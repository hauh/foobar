m0 = [
	[0, 1, 1, 0],
	[0, 0, 0, 1],
	[1, 1, 0, 0],
	[1, 1, 1, 0],
]


m1 = [
	[0, 0, 0, 0, 0, 0],
	[1, 1, 1, 1, 1, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 1, 1, 1, 1, 1],
	[0, 1, 1, 1, 1, 1],
	[0, 0, 0, 0, 0, 0]
]


def find_path(mp, width, height):
	best_lenght = width * height
	path = [(0, 0, 1)]
	while path:
		y, x, lenght = path.pop()
		if y == height - 1 and x == width - 1:
			if lenght < best_lenght:
				lenght = best_lenght
			continue
		mp[y][x] = -1
		if x > 0 and mp[y][x - 1] == 0:
			path.append((y, x - 1, lenght + 1))
		if y > 0 and mp[y - 1][x] == 0:
			path.append((y - 1, x, lenght + 1))
		if x < width - 1 and mp[y][x + 1] == 0:
			path.append((y, x + 1, lenght + 1))
		if y < height - 1 and mp[y + 1][x] == 0:
			path.append((y + 1, x, lenght + 1))
	for y in range(height):
		for x in range(width):
			if mp[y][x] == -1:
				mp[y][x] = 0
	return best_lenght


def solution(mp):
	height = len(mp)
	width = len(mp[0])
	best_path = find_path(mp, width, height)
	for x in range(width):
		for y in range(height):
			if mp[y][x] == 0:
				continue
			mp[y][x] = 0
			path = find_path(mp, width, height)
			if path < best_path:
				best_path = path
			mp[y][x] = 1
	return best_path


print(solution(m0))
print(solution(m1))
