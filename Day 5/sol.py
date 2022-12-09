# 2022 Day 5

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
        data = file.readlines()
    DATA.setdefault(key, data)


# Puzzle constants
N = 1000
ACTIONS1 = {
    "turn on": lambda _: 1,
    "toggle": lambda x: 1 - x,
    "turn off": lambda _: 0
}
ACTIONS2 = {
    "turn on": lambda x: x + 1,
    "toggle": lambda x: x + 2,
    "turn off": lambda x: 0 if x == 0 else (x - 1)
}


# Part 1 solution
def part1(arr: typing.List[str]) -> typing.Any:
    grid = [[0 for _ in range(N)] for _ in range(N)]

    for x in arr:
        match = re.search(r"^(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)$", x)
        action, (a, b, c, d) = match.group(1), map(int, match.groups()[1:])
        
        for i in range(a, c + 1):
            for j in range(b, d + 1):
                grid[i][j] = ACTIONS1[action](grid[i][j])

    return sum(map(sum, grid))


# Part 2 solution
def part2(arr: typing.List[str]) -> typing.Any:
    grid = [[0 for _ in range(N)] for _ in range(N)]

    for x in arr:
        match = re.search(r"^(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)$", x)
        action, (a, b, c, d) = match.group(1), map(int, match.groups()[1:])
        
        for i in range(a, c + 1):
            for j in range(b, d + 1):
                grid[i][j] = ACTIONS2[action](grid[i][j])

    return sum(map(sum, grid))


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
