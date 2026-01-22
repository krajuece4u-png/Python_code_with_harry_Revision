"""
Tests for 08_CONDITION - SIMPLE PROBLEMS
Run with: pytest test_simple.py -v
"""
import pytest


def test_problem_1_positive_check():
    """Test checking if number is positive"""
    num = 15
    assert num > 0


def test_problem_2_even_odd():
    """Test even/odd check"""
    num_even = 10
    num_odd = 7
    assert num_even % 2 == 0
    assert num_odd % 2 != 0


def test_problem_3_larger_number():
    """Test finding larger number"""
    a = 25
    b = 30
    larger = b if a < b else a
    assert larger == 30


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
