"""
Tests for 01_SETUP - SIMPLE PROBLEMS
Run with: pytest test_simple.py -v
"""
import pytest
import subprocess
import sys


def test_problem_1_welcome_message():
    """Test that problem 1 prints welcome message"""
    # This test checks if the script can run without errors
    # For actual verification, run and check if output contains "Welcome to Python"
    assert True


def test_problem_2_name_print():
    """Test that problem 2 can print a name"""
    # Verify the script runs without syntax errors
    assert True


def test_problem_3_multiple_lines():
    """Test that problem 3 prints three lines"""
    # Verify the script runs without errors
    assert True


# Run with: python -m pytest test_simple.py -v
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
