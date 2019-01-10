from collections import defaultdict, namedtuple
import re
from typing import DefaultDict, Dict, List, Tuple


Claim = namedtuple("Claim", ["id", "left", "top", "width", "height"])


def read_input(fname: str) -> List[Claim]:
    results = []

    with open(fname, "r") as f:
        for line in f:
            nums = [int(i) for i in re.findall(r"\d+", line)]
            claim = Claim(*nums)
            results.append(claim)
    return results


def tally_squares(claims: List[Claim]) -> Dict[Tuple[int, int], int]:
    squares: DefaultDict[Tuple[int, int], int] = defaultdict(int)
    for claim in claims:
        for x in range(claim.left, claim.left + claim.width):
            for y in range(claim.top, claim.top + claim.height):
                squares[(x, y)] += 1

    return squares


def part_1(squares: Dict[Tuple[int, int], int]) -> int:
    return len([i for i in squares.values() if i > 1])


def part_2(claims: List[Claim], squares: Dict[Tuple[int, int], int]) -> int:
    for claim in claims:
        subset = [
            (x, y)
            for x in range(claim.left, claim.left + claim.width)
            for y in range(claim.top, claim.top + claim.height)
        ]
        tally = [squares[coord] for coord in subset]
        if all(i == 1 for i in tally):
            return claim.id

    return 0


if __name__ == "__main__":

    input_file = "input.txt"
    input_data = read_input(input_file)
    squares = tally_squares(input_data)

    print("Part 1:", part_1(squares))
    print("Part 2:", part_2(input_data, squares))
