# 2022 Day 2

import re
import typing


# Environment constants
DATA_PATH = {
    "puzzle": "puzzle-data.txt",
    "test": "test-data.txt"
}
DATA = {}

for key, value in DATA_PATH.items():
    with open(value, "r", encoding="utf-8") as file:
        data = [list(map(int, re.findall("\d+", x))) for x in file.readlines()]
    DATA.setdefault(key, data)


# Puzzle constants


# Part 1 solution
def part1(arr: typing.List[typing.List[str]]) -> typing.Any:
    return sum(
        sum(2 * x[i] * x[i - 1] for i in range(len(x))) + sorted(x)[0] * sorted(x)[1] for x in arr
    )


# Part 2 solution
def part2(arr: typing.List[typing.List[str]]) -> typing.Any:
    return sum(
        2 * (sorted(x)[0] + sorted(x)[1]) + (x[0] * x[1] * x[2]) for x in arr
    )


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
