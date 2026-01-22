"""
Tests for 04_TYPECASTING - SIMPLE PROBLEMS
Run with: pytest test_simple.py -v
"""
import pytest


def test_problem_1_string_to_int():
    """Test converting string to integer"""
    num_str = "100"
    num_int = int(num_str)
    assert num_int == 100
    assert isinstance(num_int, int)


def test_problem_2_int_to_string():
    """Test converting integer to string"""
    num = 50
    num_str = str(num)
    result = "The number is " + num_str
    assert result == "The number is 50"
    assert isinstance(num_str, str)


def test_problem_3_to_float():
    """Test converting to float"""
    pi_str = "3.14"
    pi_float = float(pi_str)
    assert pi_float == pytest.approx(3.14)
    assert isinstance(pi_float, float)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
