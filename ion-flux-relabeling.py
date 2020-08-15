"""Level 2.1"""


def find(top_number, n):
	if n >= top_number:
		return -1
	med = top_number // 2
	if n < med:
		return find(med, n)
	if n > med:
		return med + find(med, n - med)
	return top_number


def solution(h, q):
	top_number = 2 ** h - 1
	return [find(top_number, n) for n in q]


for k in range(1, 6):
	print('======   ', k)
	for i in range(1, 2 ** k):
		print(i, find(2 ** k - 1, i))
