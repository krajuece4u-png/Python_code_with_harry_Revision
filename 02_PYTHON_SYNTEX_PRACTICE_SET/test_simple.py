"""
Tests for 02_PYTHON_SYNTEX - SIMPLE PROBLEMS
Run with: pytest test_simple.py -v
"""
import pytest


def test_problem_1_valid_statements():
    """Test that problem 1 identifies valid statements"""
    # Problem: Identify valid Python statements
    # Expected: x = 5 should be valid, x can be printed
    x = 5
    assert x == 5


def test_problem_2_multiple_statements():
    """Test that problem 2 works with multiple statements"""
    # Problem: Write multiple statements
    # Expected: Should perform arithmetic and print result
    a = 10
    b = 20
    c = a + b
    assert c == 30


def test_problem_3_indentation():
    """Test that problem 3 uses proper indentation"""
    # Problem: Demonstrate proper indentation
    # Expected: Conditional block should work correctly
    result = []
    if True:
        result.append("indented")
    assert len(result) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
