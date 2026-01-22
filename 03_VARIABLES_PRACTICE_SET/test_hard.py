"""
Tests for 03_VARIABLES - HARD PROBLEMS
Run with: pytest test_hard.py -v
"""
import pytest


def test_problem_1_dynamic_assignment():
    """Test dynamic variable operations"""
    numbers = [10, 20, 30, 40, 50]
    min_val = min(numbers)
    max_val = max(numbers)
    sum_val = sum(numbers)
    avg_val = sum_val / len(numbers)
    assert min_val == 10
    assert max_val == 50
    assert sum_val == 150
    assert avg_val == 30


def test_problem_2_nested_operations():
    """Test nested variable operations"""
    principal = 1000
    rate = 5
    time = 2
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest
    assert simple_interest == 100
    assert total_amount == 1100


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
