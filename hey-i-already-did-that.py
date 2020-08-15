"""Level 2.2"""


def substract(n, base):
	x = sorted(n)
	y = sorted(n, reverse=True)
	debt = 0
	z = []
	for a, b in zip(x, y):
		b += debt
		if a < b:
			debpt = 1
			a += base
		else:
			debt = 0
		z.append(a - b)
	return list(reversed(z))


def loop(n, b, history):
	z = substract(n, b)
	if z in history:
		iterations = 1
		while history[-1] != z:
			history.pop()
			iterations += 1
		return iterations
	history.append(z)
	return loop(z, b, history)


def solution(n, b):
	n = [int(digit) for digit in n]
	return loop(n, b, [n])
