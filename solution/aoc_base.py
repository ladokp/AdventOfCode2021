# aoc_base.py

import pathlib
from abc import ABC, abstractmethod


class AocBaseClass(ABC):
    def __init__(self, /, test_suffix=""):
        path = f"{pathlib.Path(__file__).parent.parent}/resources/day_{self.__class__.get_day():02}{test_suffix}.txt"
        puzzle_input = pathlib.Path(path).read_text().strip()
        self.data = self._parse(puzzle_input)
        self.solutions = None

    @classmethod
    @abstractmethod
    def get_day(cls):
        """Parse input"""
        return cls.day

    @abstractmethod
    def _parse(self, puzzle_input):
        """Parse input"""
        pass

    @abstractmethod
    def part1(self):
        """Solve part 1"""
        pass

    @abstractmethod
    def part2(self):
        """Solve part 2"""
        pass

    def solve(self):
        """Solve the puzzle for the given input"""
        self.solutions = self.part1(), self.part2()
