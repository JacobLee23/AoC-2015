# 2022 Day 11

import collections
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
        data = file.read()
    DATA.setdefault(key, data)


# Puzzle constants


def is_valid(s: str) -> bool:
    conditions = [
        any(
            string.ascii_lowercase[i:(i + 3)] in s
            for i in range(len(string.ascii_lowercase) - 2)
        ),
        not any(x in s for x in "iol"),
        len(re.findall(r"([a-z])\1", s)) >= 2
    ]
    return all(conditions)


def wrap_characters(d: collections.deque) -> collections.deque:
    i = len(d) - 1

    while i >= 0:
        if d[i] >= len(string.ascii_lowercase):
            d[i] -= len(string.ascii_lowercase)
            if i == 0:
                d.appendleft(0)
            d[i - 1] += 1

        i -= 1

    return d


def increment_password(d: collections.deque) -> collections.deque:
    d[-1] += 1
    d = wrap_characters(d)


def find_next(s: str) -> str:
    d = collections.deque(string.ascii_lowercase.index(c) for c in s)

    while True:
        d[-1] += 1
        d = wrap_characters(d)

        for i, c in enumerate(d):
            if string.ascii_lowercase[c] in "iol":
                d[i] += 1
                d = wrap_characters(
                    collections.deque(0 if j >= (i + 1) else d[j] for j in range(len(d)))
                )
                break

        password = "".join(string.ascii_lowercase[i] for i in d)
        if is_valid(password):
            return password


# Part 1 solution
def part1(arr: str) -> str:
    return find_next(arr)


# Part 2 solution
def part2(arr: str) -> str:
    return find_next(find_next(arr))


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
