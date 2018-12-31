"""
2017 Day 1: Inverse Captcha
"""

def part_1(num):
    num_str = str(num)
    num_len = len(num_str)

    total = 0
    for i in range(num_len):
        j = i + 1 if i < num_len - 1 else 0
        if num_str[i] == num_str[j]:
            total += int(num_str[i])
    return total

def part_2(num):
    num_str = str(num)
    num_len = len(num_str)
    half = num_len // 2

    total = 0

    for i in range(num_len):
        j = i + half
        if j >= num_len:
            j = (i + half) % num_len
        if num_str[i] == num_str[j]:
            total += int(num_str[i])
    return total

if __name__ == "__main__":
    INPUT = input("Puzzle input: ")

    with open(INPUT, "r") as f:
        NUM = int(f.read())

    print("Part 1: ", end="")
    print(part_1(NUM))
    print("Part 2: ", end="")
    print(part_2(NUM))

