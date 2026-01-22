"""
Tests for 02_PYTHON_SYNTEX - MODERATE PROBLEMS
Run with: pytest test_moderate.py -v
"""
import pytest


def test_problem_1_multiline_statements():
    """Test multi-line statement syntax"""
    result = (10 + 20 +
              30 + 40)
    assert result == 100


def test_problem_2_multiple_one_line():
    """Test multiple statements on one line"""
    x = 5; y = 10; z = x + y
    assert z == 15


def test_problem_3_backslash_continuation():
    """Test backslash line continuation"""
    message = "This is a long " \
              "string that continues " \
              "on multiple lines"
    assert "long" in message
    assert "multiple lines" in message


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
