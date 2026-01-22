"""
Tests for 12_LIST - HARD PROBLEMS
Run with: pytest test_hard.py -v
"""
import pytest


def test_problem_1_nested_lists():
    """Test nested lists"""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert matrix[1][2] == 6
    
    flat = [item for row in matrix for item in row]
    assert flat == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_problem_2_advanced_operations():
    """Test advanced list operations"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    result = [x**2 for x in numbers if x % 2 == 0]
    assert result == [4, 16, 36, 64, 100]
    
    doubled = list(map(lambda x: x * 2, numbers))
    assert doubled == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
