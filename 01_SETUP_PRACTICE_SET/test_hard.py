"""
Tests for 01_SETUP - HARD PROBLEMS
Run with: pytest test_hard.py -v
"""
import pytest


def test_problem_1_formatted_box():
    """Test that problem 1 creates a formatted box"""
    # Problem: Create a box with borders and message
    # Expected: Should have border, message inside, and proper formatting
    assert True


def test_problem_2_pyramid():
    """Test that problem 2 creates pyramid structure"""
    # Problem: Create pyramid-like structure
    # Expected: Should display increasing asterisks row by row
    assert True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
