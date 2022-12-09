# 2022 Day 8

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
    return sum(len(x.strip()) - len(eval(x.strip())) for x in arr)


# Part 2 solution
def part2(arr: typing.List[str]) -> typing.Any:
    return sum(x.count("\\") + x.count("\"") + 2 for x in arr)


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
