"""
Tests for 07_OPERATORS - MODERATE PROBLEMS
Run with: pytest test_moderate.py -v
"""
import pytest


def test_problem_1_comparison():
    """Test comparison operators"""
    a = 10
    b = 20
    assert not (a == b)
    assert a != b
    assert a < b
    assert not (a > b)
    assert a <= b
    assert b >= a


def test_problem_2_logical():
    """Test logical operators"""
    x = 15
    assert x > 10 and x < 20
    assert not (x < 10 or x > 20)
    assert not (x > 20)


def test_problem_3_assignment():
    """Test assignment operators"""
    num = 10
    num += 5
    assert num == 15
    num -= 3
    assert num == 12
    num *= 2
    assert num == 24


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
