# test_aoc_day_17.py

import pytest
import solution.aoc_day_17 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test that input is parsed properly"""
    assert test_solution.data == (20, 30, -10, -5)


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1()[0] == 45


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2()[1] == 112


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1()[0] == 4005


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2()[1] == 2953
