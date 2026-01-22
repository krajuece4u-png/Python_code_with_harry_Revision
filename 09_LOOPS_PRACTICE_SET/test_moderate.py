"""
Tests for 09_LOOPS - MODERATE PROBLEMS
Run with: pytest test_moderate.py -v
"""
import pytest


def test_problem_1_star_pattern():
    """Test star pattern creation"""
    pattern = []
    for i in range(1, 6):
        pattern.append("*" * i)
    assert len(pattern) == 5
    assert pattern[0] == "*"
    assert pattern[4] == "*****"


def test_problem_2_factorial():
    """Test factorial calculation"""
    n = 5
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    assert factorial == 120


def test_problem_3_break_continue():
    """Test break and continue"""
    # Break test
    break_result = []
    for i in range(1, 6):
        if i == 3:
            break
        break_result.append(i)
    assert break_result == [1, 2]
    
    # Continue test
    continue_result = []
    for i in range(1, 6):
        if i == 3:
            continue
        continue_result.append(i)
    assert continue_result == [1, 2, 4, 5]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
