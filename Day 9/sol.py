# 2022 Day 9

import collections
import itertools
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


def get_routes(arr: typing.List[str]) -> collections.defaultdict:
    d = collections.defaultdict()

    for x in arr:
        groups = re.search(r"^(\w+) to (\w+) = (\d+)$", x).groups()
        d[(groups[0], groups[1])] = d[(groups[1], groups[0])] = int(groups[2])

    return d


# Part 1 solution
def part1(arr: typing.List[str]) -> typing.Any:
    d = get_routes(arr)
    cities = list({x[0] for x in d})

    return min(
        sum(d[(a, b)] for a, b in zip(x[:-1], x[1:]))
        for x in itertools.permutations(cities, len(cities))
    )


# Part 2 solution
def part2(arr: typing.List[str]) -> typing.Any:
    d = get_routes(arr)
    cities = list({x[0] for x in d})

    return max(
        sum(d[(a, b)] for a, b in zip(x[:-1], x[1:]))
        for x in itertools.permutations(cities, len(cities))
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
