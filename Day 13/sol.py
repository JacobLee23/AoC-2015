# 2022 Day 13

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


def parse_data(arr: typing.List[str]) -> collections.defaultdict:
    d = collections.defaultdict()

    for line in arr:
        x = re.search(
            r"^(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.$",
            line
        )
        d[(x.group(1), x.group(4))] = (1 if x.group(2) == "gain" else -1) * int(x.group(3))
        
    return d


# Part 1 solution
def part1(arr: typing.List[str]) -> int:
    d = parse_data(arr)
    names = list({x[0] for x in d})

    return max(
        sum(
            d[p] + d[tuple(p[::-1])] for p in itertools.pairwise(x)
        ) + d[(x[-1], x[0])] + d[(x[0], x[-1])]
        for x in itertools.permutations(names)
    )


# Part 2 solution
def part2(arr: typing.List[str]) -> int:
    d = parse_data(arr)
    names = list({x[0] for x in d})

    return max(
        sum(
            d[p] + d[tuple(p[::-1])] for p in itertools.pairwise(x)
        )
        for x in itertools.permutations(names)
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
