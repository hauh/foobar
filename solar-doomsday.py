"""Level 1"""


def root(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x ** 2


def solution(area):
    squares = []
    while area:
        max_square = root(area)
        squares.append(max_square)
        area -= max_square
    return squares
