# 2022 Day 5

import re
import string
import typing


# Environment constants
DATA_PATH = {
    "puzzle": "puzzle-data.txt",
    "test": "test-data.txt"
}
DATA = {}

for key, value in DATA_PATH.items():
    with open(value, "r", encoding="utf-8") as file:
        data = file.readlines()
    DATA.setdefault(key, data)


# Puzzle constants


# Part 1 solution
def part1(arr: typing.List[str]) -> typing.Any:
    conditions = [
        lambda x: len(re.findall("[aeiou]", x)) >= 3,
        lambda x: re.search(r"([a-z])\1", x) is not None,
        lambda x: not any(s in x for s in ["ab", "cd", "pq", "xy"])
    ]

    return len(list(filter(lambda x: all(f(x) for f in conditions), arr)))


# Part 2 solution
def part2(arr: typing.List[str]) -> typing.Any:
    conditions = [
        lambda x: re.search(r"([a-z]{2})[a-z]*\1", x) is not None,
        lambda x: re.search(r"([a-z])[a-z]\1", x) is not None
    ]

    return len(list(filter(lambda x: all(f(x) for f in conditions), arr)))


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
