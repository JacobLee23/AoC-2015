# 2022 Day 4

import hashlib
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
N1 = 5
N2 = 6

# Part 1 solution
def part1(arr: str) -> typing.Any:
    i = 1
    while True:
        if hashlib.md5(f"{arr}{i}".encode()).hexdigest().startswith("0" * N1):
            return i
        i += 1


# Part 2 solution
def part2(arr: str) -> typing.Any:
    i = 1
    while True:
        if hashlib.md5(f"{arr}{i}".encode()).hexdigest().startswith("0" * N2):
            return i
        i += 1


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
