# 2022 Day 1

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
DIRECTION = {"(": 1, ")": -1}


# Part 1 solution
def part1(arr: typing.List[str] = DATA) -> typing.Any:
    return sum(DIRECTION[x] for x in arr)


# Part 2 solution
def part2(arr: typing.List[str] = DATA) -> typing.Any:
    position = [DIRECTION[x] for x in arr]
    for i in range(1, len(position)):
        position[i] += position[i - 1]
    return position.index(-1) + 1


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
