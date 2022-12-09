# 2022 Day 10

import itertools
import typing


# Environment constants
DATA_PATH = {
    "puzzle": "puzzle-data.txt",
    "test": "test-data.txt"
}
DATA = {}

for key, value in DATA_PATH.items():
    with open(value, "r", encoding="utf-8") as file:
        data = file.read()
    DATA.setdefault(key, data)


# Puzzle constants


def expand(arr: str) -> str:
    nums = (
        (label, sum(1 for _ in group))
        for label, group in itertools.groupby(arr)
    )
    return "".join(f"{b}{a}" for a, b in nums)


# Part 1 solution
def part1(arr: str) -> int:
    x = arr
    for _ in range(40):
        x = expand(x)

    return len(x)


# Part 2 solution
def part2(arr: typing.List[str]) -> typing.Any:
    x = arr
    for _ in range(50):
        x = expand(x)

    return len(x)


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
