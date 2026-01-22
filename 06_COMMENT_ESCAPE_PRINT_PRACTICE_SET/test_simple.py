"""
Tests for 06_COMMENT_ESCAPE_PRINT - SIMPLE PROBLEMS
Run with: pytest test_simple.py -v
"""
import pytest


def test_problem_1_arithmetic():
    """Test basic arithmetic"""
    x = 10
    y = 20
    assert x + y == 30


def test_problem_2_escape_sequences():
    """Test escape sequences work"""
    text1 = "Hello\nWorld"
    assert "\n" in text1
    text2 = "Name\tAge"
    assert "\t" in text2


def test_problem_3_print_formats():
    """Test print with different formats"""
    result = []
    result.append("A")
    result.append("B")
    result.append("C")
    assert len(result) == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
