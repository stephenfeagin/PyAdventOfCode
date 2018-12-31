"""
2017 Day 2: Corruption Checksum
"""

from itertools import permutations

def read_input(fname):
    with open(fname, "r") as f:
        data = [line.split("\t") for line in f.readlines()]
    for i in range(len(data)):
        data[i] = [int(num) for num in data[i]]
    return data

def part_1(data):
    total = 0
    for row in data:
        total += (max(row) - min(row))

    return total

def part_2(data):
    total = 0
    for row in data:
        perms = permutations(row, 2)
        for pair in perms:
            if pair[0] % pair[1] == 0:
                total += pair[0] // pair[1]
    return total

