"""
Tests for 10_STRINGS - SIMPLE PROBLEMS
Run with: pytest test_simple.py -v
"""
import pytest


def test_problem_1_string_concatenation():
    """Test string concatenation"""
    str1 = "Hello"
    str2 = "World"
    result = str1 + " " + str2
    assert result == "Hello World"


def test_problem_2_string_length():
    """Test string length"""
    text = "Python"
    assert len(text) == 6


def test_problem_3_string_indexing():
    """Test string indexing"""
    name = "Python"
    assert name[0] == "P"
    assert name[-1] == "n"
    assert name[2] == "t"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
