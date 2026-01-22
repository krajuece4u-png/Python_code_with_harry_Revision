"""
Tests for 09_LOOPS - SIMPLE PROBLEMS
Run with: pytest test_simple.py -v
"""
import pytest


def test_problem_1_print_range():
    """Test printing numbers in range"""
    result = list(range(1, 6))
    assert result == [1, 2, 3, 4, 5]


def test_problem_2_multiplication_table():
    """Test multiplication table"""
    table = [5 * i for i in range(1, 11)]
    assert len(table) == 10
    assert table[0] == 5
    assert table[9] == 50


def test_problem_3_sum_numbers():
    """Test sum of numbers"""
    total = sum(range(1, 11))
    assert total == 55


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
