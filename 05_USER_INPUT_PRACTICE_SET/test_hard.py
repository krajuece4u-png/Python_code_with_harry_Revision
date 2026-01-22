"""
Tests for 05_USER_INPUT - HARD PROBLEMS
Run with: pytest test_hard.py -v
"""
import pytest


def test_problem_1_valid_number():
    """Test validating numeric input"""
    def get_valid_number(value_str):
        try:
            return float(value_str)
        except ValueError:
            return None
    
    assert get_valid_number("10.5") == 10.5
    assert get_valid_number("abc") is None
    assert get_valid_number("100") == 100.0


def test_problem_2_calculator():
    """Test simple calculator logic"""
    def calculate(num1, operator, num2):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        return None
    
    assert calculate(10, '+', 5) == 15
    assert calculate(10, '-', 3) == 7
    assert calculate(4, '*', 5) == 20
    assert calculate(20, '/', 4) == 5.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
