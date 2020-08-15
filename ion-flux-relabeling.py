"""Level 2.1"""


def find(top_number, n):
	if n >= top_number:
		return -1
	if n == top_number - 1:
		return top_number
	med = top_number // 2
	if n < med:
		return find(med, n)
	if n > med:
		return med + find(med, n - med)
	return top_number


def solution(h, q):
	top_number = 2 ** h - 1
	return [find(top_number, n) for n in q]
