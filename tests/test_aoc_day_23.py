# test_aoc_day_23.py

import pytest
import solution.aoc_day_23 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test that input is parsed properly"""
    assert test_solution.data is not None


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 12521


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == 44169


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 19019


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 47533
