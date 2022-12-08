# Usage: $ setupnew.py <day> ...

from dataclasses import dataclass
import os
import pathlib
import sys
import typing


YEAR = 2022


TEMPLATE_PATH = pathlib.Path("py-template.txt")

with open(TEMPLATE_PATH, "r", encoding="utf-8") as file:
    TEMPLATE = file.read()


@dataclass
class Day:
    day: int

    def __repr__(self) -> str:
        return f"Day(day={self.day}, dir_path='{self.dir_path}', file_paths='{self.file_paths}')"

    @property
    def dir_path(self) -> pathlib.Path:
        return pathlib.Path(f"Day {self.day}")

    @property
    def py_path(self) -> pathlib.Path:
        return self.dir_path / "sol.py"

    @property
    def puzzle_data_path(self) -> pathlib.Path:
        return self.dir_path / "puzzle-data.txt"

    @property
    def test_data_path(self) -> pathlib.Path:
        return self.dir_path / "test-data.txt"

    @property
    def file_paths(self) -> typing.List[pathlib.Path]:
        return [self.py_path, self.puzzle_data_path, self.test_data_path]


def setup_day(n: int) -> Day:
    day = Day(n)

    try:
        os.mkdir(day.dir_path)
    except OSError:
        return

    for path in day.file_paths:
        open(path, "w", encoding="utf-8").close()

    with open(day.py_path, "w", encoding="utf-8") as file:
        file.write(
            TEMPLATE.format(
                year=YEAR,
                day=day.day,
                puzzle_data_path=day.puzzle_data_path.relative_to(day.dir_path).as_posix(),
                test_data_path=day.test_data_path.relative_to(day.dir_path).as_posix()
            )
        )

    return day


def main(*args):
    for n in args:
        day = setup_day(int(n))
        print(day)


if __name__ == "__main__":
    main(*sys.argv[1:])
