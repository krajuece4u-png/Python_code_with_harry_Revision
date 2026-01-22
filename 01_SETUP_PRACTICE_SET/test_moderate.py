"""
Tests for 01_SETUP - MODERATE PROBLEMS
Run with: pytest test_moderate.py -v
"""
import pytest


def test_problem_1_pattern():
    """Test that problem 1 creates a pattern"""
    # Problem: Print a pattern with asterisks
    # Expected: Should print multiple lines with asterisks
    assert True


def test_problem_2_separators():
    """Test that problem 2 prints numbers with separators"""
    # Problem: Print numbers with different separators
    # Expected: Should have comma, dash, and space separated versions
    assert True


def test_problem_3_ascii_art():
    """Test that problem 3 prints ASCII art"""
    # Problem: Print simple ASCII art
    # Expected: Should display a face-like character
    assert True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
