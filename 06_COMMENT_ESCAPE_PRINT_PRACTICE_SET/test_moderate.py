"""
Tests for 06_COMMENT_ESCAPE_PRINT - MODERATE PROBLEMS
Run with: pytest test_moderate.py -v
"""
import pytest


def test_problem_1_function_documentation():
    """Test function with docstring"""
    def add(a, b):
        '''
        This function adds two numbers
        Parameters: a, b (numbers)
        Returns: sum of a and b
        '''
        return a + b
    
    assert add(5, 10) == 15
    assert add.__doc__ is not None


def test_problem_2_escape_sequences():
    """Test complex escape sequences"""
    # Test newlines
    text = "Line 1\nLine 2\nLine 3"
    lines = text.split("\n")
    assert len(lines) == 3
    
    # Test tabs
    text_tab = "Col1\tCol2\tCol3"
    assert "\t" in text_tab


def test_problem_3_table_format():
    """Test table formatting"""
    rows = [
        "Name\tAge\tCity",
        "---\t---\t---",
        "John\t25\tNY",
        "Jane\t30\tLA"
    ]
    assert len(rows) == 4
    assert all("\t" in row for row in rows)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
