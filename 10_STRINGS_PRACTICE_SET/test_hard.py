"""
Tests for 10_STRINGS - HARD PROBLEMS
Run with: pytest test_hard.py -v
"""
import pytest


def test_problem_1_fstring_formatting():
    """Test f-string formatting"""
    name = "Alice"
    score = 95.5
    formatted = f"Student: {name}, Score: {score:.1f}%"
    assert "Alice" in formatted
    assert "95.5" in formatted


def test_problem_2_string_manipulation():
    """Test string manipulation"""
    sentence = "  hello world from python  "
    cleaned = sentence.strip().title()
    assert cleaned == "Hello World From Python"
    
    text = "banana"
    count = text.count('a')
    assert count == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
