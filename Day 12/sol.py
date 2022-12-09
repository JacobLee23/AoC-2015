# 2022 Day 12

import json
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
        data = file.read()
    DATA.setdefault(key, data)


# Puzzle constants


def sum_array(a: typing.List) -> int:
    res = 0

    for x in a:
        if isinstance(x, int):
            res += x
        elif isinstance(x, str):
            continue
        elif isinstance(x, list):
            res += sum_array(x)
        elif isinstance(x, dict):
            res += sum_dict(x)
        else:
            raise TypeError

    return res


def sum_dict(d: typing.Dict) -> int:
    res = 0

    if "red" in d.values():
        return 0

    for v in d.values():
        if isinstance(v, int):
            res += v
        elif isinstance(v, str):
            continue
        elif isinstance(v, list):
            res += sum_array(v)
        elif isinstance(v, dict):
            res += sum_dict(v)
        else:
            raise TypeError

    return res


# Part 1 solution
def part1(arr: str) -> int:
    return sum(map(int, re.findall(r"[0-9-]+", arr)))


# Part 2 solution
def part2(arr: typing.List[str]) -> typing.Any:
    return sum_array(json.loads(arr))


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
