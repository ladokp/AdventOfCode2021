# test_aoc_day_05.py

import pytest
import solution.aoc_day_05 as aoc

aoc_day_solution = aoc.AocSolution()
aoc_day_solution_test = aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def example1():
    return aoc_day_solution_test.data


@pytest.fixture
def exercise_data():
    return aoc_day_solution.data


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 is None


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc_day_solution_test.part1() == 5


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc_day_solution_test.part2() == 12


def test_part1_exercise_data(exercise_data):
    """Test part 1 on exercise_data input"""
    assert aoc_day_solution.part1() == 5306


def test_part2_exercise_data(exercise_data):
    """Test part 2 on exercise_data input"""
    assert aoc_day_solution.part2() == 17787