"""
Tests for 07_OPERATORS - SIMPLE PROBLEMS
Run with: pytest test_simple.py -v
"""
import pytest


def test_problem_1_arithmetic():
    """Test basic arithmetic operations"""
    a = 20
    b = 5
    assert a + b == 25
    assert a - b == 15
    assert a * b == 100
    assert a / b == 4.0


def test_problem_2_modulus_exponent():
    """Test modulus and exponentiation"""
    x = 17
    y = 5
    assert x % y == 2
    assert 2 ** 3 == 8


def test_problem_3_floor_division():
    """Test floor division"""
    assert 17 // 5 == 3
    assert 25 // 4 == 6


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
