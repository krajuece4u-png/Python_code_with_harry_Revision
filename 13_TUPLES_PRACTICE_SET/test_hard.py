"""
Tests for 13_TUPLES - HARD PROBLEMS
Run with: pytest test_hard.py -v
"""
import pytest
from collections import namedtuple


def test_problem_1_dict_keys():
    """Test tuples as dictionary keys"""
    coordinates = {
        (0, 0): "origin",
        (1, 0): "positive x",
        (0, 1): "positive y",
        (1, 1): "first quadrant"
    }
    assert coordinates[(1, 1)] == "first quadrant"
    assert coordinates[(0, 0)] == "origin"


def test_problem_2_named_tuples():
    """Test named tuples"""
    Point = namedtuple('Point', ['x', 'y'])
    p1 = Point(10, 20)
    assert p1.x == 10
    assert p1.y == 20
    assert p1[0] == 10


def test_problem_3_unpacking():
    """Test advanced unpacking"""
    data = (1, 2, 3, 4, 5)
    first, *middle, last = data
    assert first == 1
    assert middle == [2, 3, 4]
    assert last == 5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
