"""
Tests for 03_VARIABLES - SIMPLE PROBLEMS
Run with: pytest test_simple.py -v
"""
import pytest


def test_problem_1_variable_creation():
    """Test creating and printing variables"""
    name = "Alice"
    age = 25
    city = "London"
    assert name == "Alice"
    assert age == 25
    assert city == "London"


def test_problem_2_swap_variables():
    """Test swapping two variables"""
    a = 10
    b = 20
    a, b = b, a
    assert a == 20
    assert b == 10


def test_problem_3_multiple_assignment():
    """Test multiple variable assignment"""
    x, y, z = 5, 10, 15
    assert x == 5
    assert y == 10
    assert z == 15


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
