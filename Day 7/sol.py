# 2022 Day 7

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
BITWISE = {
    "INIT": re.compile(r"^([0-9a-z]+) -> ([a-z]+)$"),
    "NOT": re.compile(r"^NOT ([a-z]+) -> ([a-z]+)$"),
    "AND": re.compile(r"^([0-9a-z]+) AND ([0-9a-z]+) -> ([a-z]+)$"),
    "OR": re.compile(r"^([0-9a-z]+) OR ([0-9a-z]+) -> ([a-z]+)$"),
    "RSHIFT": re.compile(r"^([a-z]+) RSHIFT (\d+) -> ([a-z]+)$"),
    "LSHIFT": re.compile(r"^([a-z]+) LSHIFT (\d+) -> ([a-z]+)$")
}


def logic(d: collections.defaultdict, operation: str, *comp: typing.Union[int, str]) -> typing.Tuple[str, int]:
    if operation == "INIT":
        a, b = comp
        return b, a if isinstance(a, int) else d[a]
    elif operation == "NOT":
        a, b = comp
        n = ~d[a]
        return b, 65536 - abs(n) if n < 0 else n
    elif operation == "AND":
        a, b, c = comp
        a = a if isinstance(a, int) else d[a]
        b = b if isinstance(b, int) else d[b]
        return c, a & b
    elif operation == "OR":
        a, b, c = comp
        a = a if isinstance(a, int) else d[a]
        b = b if isinstance(b, int) else d[b]
        return c, a | b
    elif operation == "LSHIFT":
        a, b, c = comp
        return c, d[a] << b
    elif operation == "RSHIFT":
        a, b, c = comp
        return c, d[a] >> b
    else:
        raise ValueError


def assemble(d: collections.defaultdict, arr: typing.List[str]) -> collections.defaultdict:
    while arr:
        for line in arr:
            bitwise = {k: v.search(line) for k, v in BITWISE.items()}
            operation, match = list(filter(lambda x: x[1] is not None, bitwise.items()))[0]
            components = [int(x) if x.isdecimal() else x for x in match.groups()]

            try:
                key, value = logic(d, operation, *components)
            except KeyError:
                continue

            d.setdefault(key, value)
            arr.remove(line)

    return d


# Part 1 solution
def part1(arr: typing.List[str]) -> typing.Any:
    d = collections.defaultdict()
    return assemble(d, arr[:]).get("a")


# Part 2 solution
def part2(arr: typing.List[str]) -> typing.Any:
    d = collections.defaultdict()
    d["b"] = part1(arr)
    return assemble(d, arr[:]).get("a")


def main():
    print("Test data:")
    print(f"\tPart 1:\t{part1(DATA['test'])}")
    print(f"\tPart 2:\t{part2(DATA['test'])}")
    print("Puzzle data:")
    print(f"\tPart 1:\t{part1(DATA['puzzle'])}")
    print(f"\tPart 2:\t{part2(DATA['puzzle'])}")


if __name__ == "__main__":
    main()
