"""
Tests for 04_TYPECASTING - MODERATE PROBLEMS
Run with: pytest test_moderate.py -v
"""
import pytest


def test_problem_1_cast_and_calculate():
    """Test casting and calculating with integers"""
    num1_str = "20"
    num2_str = "30"
    num1 = int(num1_str)
    num2 = int(num2_str)
    result = num1 + num2
    assert result == 50


def test_problem_2_mixed_type_operations():
    """Test mixed type operations"""
    a = 10
    b = 3.5
    c = float(a)
    total = c + b
    assert total == 13.5
    assert isinstance(total, float)


def test_problem_3_boolean_to_integer():
    """Test converting boolean to integer"""
    is_valid = True
    is_empty = False
    val1 = int(is_valid)
    val2 = int(is_empty)
    assert val1 == 1
    assert val2 == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
