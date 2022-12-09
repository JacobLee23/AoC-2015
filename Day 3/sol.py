# 2022 Day 3

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
DIRECTIONS = {
    "^": lambda x, y: (x, y + 1),
    "<": lambda x, y: (x - 1, y),
    "v": lambda x, y: (x, y - 1),
    ">": lambda x, y: (x + 1, y)
}


# Part 1 solution
def part1(arr: str) -> typing.Any:
    positions = [(0, 0)]

    for x in arr:
        positions.append(DIRECTIONS[x](*positions[-1]))

    return len(set(positions))


# Part 2 solution
def part2(arr: str) -> typing.Any:
    positions = [(0, 0), (0, 0)]

    for x in arr:
        positions.append(DIRECTIONS[x](*positions[-2]))

    return len(set(positions))


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
