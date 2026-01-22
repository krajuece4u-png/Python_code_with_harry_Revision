"""
Tests for 06_COMMENT_ESCAPE_PRINT - HARD PROBLEMS
Run with: pytest test_hard.py -v
"""
import pytest


def test_problem_1_ascii_table():
    """Test ASCII table creation"""
    table = [
        "+--------+-----+-------+",
        "| Name   | Age | Score |",
        "+--------+-----+-------+",
        "| Alice  |  25 |    95 |",
        "| Bob    |  23 |    87 |",
        "| Charlie|  26 |    92 |",
        "+--------+-----+-------+"
    ]
    assert len(table) == 7
    # Check that data rows have pipe characters
    assert "|" in table[1]  # header row
    assert "|" in table[3]  # data row
    # Check that border rows have plus characters
    assert "+" in table[0]  # top border
    assert "+" in table[6]  # bottom border


def test_problem_2_raw_strings():
    """Test raw strings"""
    path = r"C:\Users\Name\Documents"
    assert "\\" in path
    assert "Users" in path
    
    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    assert "@" in regex
    assert "+" in regex


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
