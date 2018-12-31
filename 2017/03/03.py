"""
2017 Day 3: Spiral Memory
"""

from math import sqrt

def get_squares(target):
    base = 1
    squares = [1]
    while squares[-1] < target:
        base += 2
        squares.append(base ** 2)
    return squares

def generate_row(max_num):
    line = []
    i = max_num
    base = sqrt(max_num)
    while len(line) < base:
        line.append(i)
        i -= 1
    line.reverse()
    return line

def generate_square_rows(max_num):
    square_list = get_squares(max_num)
    return [generate_row(i) for i in square_list]

if __name__ == "__main__":
    INPUT = "input/day_03.txt"
    with open(INPUT, "r") as f:
        NUM = int(f.read())

