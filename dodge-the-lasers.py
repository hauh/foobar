"""Level 5.1"""


def sqrt2_fraction(precision):
	digits = []
	approx = 2
	root = 0
	while precision:
		for x in range(9, -1, -1):
			check = (root * 20 + x) * x
			if check < approx:
				break
		digits.append(x)
		root = root * 10 + x
		approx = (approx - check) * 100
		precision -= 1
	return digits[1:]


def solution(str_n):
	fraction = sqrt2_fraction(len(str_n) + 3)

	def multiply_fraction(x):
		increment = 0
		for digit in reversed(fraction):
			increment = (digit * x + increment) // 10
		return increment

	def beatty_sum(n):
		if n == 0:
			return 0
		m = multiply_fraction(n)
		return n * m + n * (n + 1) // 2 - m * (m + 1) // 2 - beatty_sum(m)

	return str(beatty_sum(int(str_n)))
