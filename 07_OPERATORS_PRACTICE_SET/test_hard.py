"""
Tests for 07_OPERATORS - HARD PROBLEMS
Run with: pytest test_hard.py -v
"""
import pytest


def test_problem_1_precedence():
    """Test operator precedence"""
    result1 = 2 + 3 * 4 - 5
    assert result1 == 9
    
    result2 = (2 + 3) * (4 - 5)
    assert result2 == -5
    
    result3 = 2 + 3 * 4 ** 2 - 5
    assert result3 == 45


def test_problem_2_complex_logic():
    """Test complex logical conditions"""
    age = 25
    income = 50000
    has_credit = True
    approved = (age >= 18) and (income >= 30000) and (has_credit)
    assert approved is True
    
    score = 75
    attendance = 85
    passed = (score >= 60) and (attendance >= 80)
    assert passed is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
