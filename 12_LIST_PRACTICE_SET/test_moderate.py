"""
Tests for 12_LIST - MODERATE PROBLEMS
Run with: pytest test_moderate.py -v
"""
import pytest


def test_problem_1_list_methods():
    """Test list methods"""
    nums = [3, 1, 4, 1, 5, 9]
    assert nums.count(1) == 2
    assert nums.index(3) == 0


def test_problem_2_comprehension():
    """Test list comprehension"""
    squares = [x**2 for x in range(1, 6)]
    assert squares == [1, 4, 9, 16, 25]
    
    evens = [x for x in range(1, 11) if x % 2 == 0]
    assert evens == [2, 4, 6, 8, 10]


def test_problem_3_combine_lists():
    """Test combining lists"""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = list1 + list2
    assert combined == [1, 2, 3, 4, 5, 6]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
