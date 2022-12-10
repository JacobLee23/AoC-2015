# 2022 Day 14

import collections
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
TOTTIME = 2503


def parse_data(arr: typing.List[str]) -> collections.defaultdict:
    d = collections.defaultdict()

    for line in arr:
        x = re.search(
            r"^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.$",
            line
        ).groups()

        d[x[0]] = tuple(map(int, x[1:]))

    return d


def get_distances(d: collections.defaultdict, t: int) -> collections.defaultdict:
    return collections.defaultdict(
        int, {
            k: sum(
                [
                    t // (d[k][1] + d[k][2]) * d[k][1] * d[k][0],
                    min([t % (d[k][1] + d[k][2]), d[k][1]]) * d[k][0]
                ]
            )
            for k in d
        }
    )


def get_points(d: collections.defaultdict, t: int) -> collections.defaultdict:
    points = collections.defaultdict(int, {k: 0 for k in d})

    for i in range(1, t + 1):
        distances = get_distances(d, i)
        for x in filter(
            lambda x: distances[x] == max(distances.values()),
            distances
        ):
            points[x] += 1

    return points


# Part 1 solution
def part1(arr: typing.List[str]) -> int:
    d = parse_data(arr)
    return max(get_distances(d, TOTTIME).values())


# Part 2 solution
def part2(arr: typing.List[str]) -> int:
    d = parse_data(arr)
    return max(get_points(d, TOTTIME).values())


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
