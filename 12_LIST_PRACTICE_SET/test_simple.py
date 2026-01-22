"""
Tests for 12_LIST - SIMPLE PROBLEMS
Run with: pytest test_simple.py -v
"""
import pytest


def test_problem_1_list_creation():
    """Test list creation and access"""
    fruits = ["apple", "banana", "orange"]
    assert len(fruits) == 3
    assert fruits[0] == "apple"


def test_problem_2_indexing():
    """Test list indexing"""
    numbers = [10, 20, 30, 40, 50]
    assert numbers[0] == 10
    assert numbers[-1] == 50
    assert numbers[2] == 30


def test_problem_3_slicing():
    """Test list slicing"""
    items = [1, 2, 3, 4, 5, 6, 7, 8]
    assert items[:3] == [1, 2, 3]
    assert items[-2:] == [7, 8]
    assert items[2:5] == [3, 4, 5]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
