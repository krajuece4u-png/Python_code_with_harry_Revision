"""
Tests for 10_STRINGS - MODERATE PROBLEMS
Run with: pytest test_moderate.py -v
"""
import pytest


def test_problem_1_slicing():
    """Test string slicing"""
    text = "Hello World"
    assert text[:5] == "Hello"
    assert text[-5:] == "World"
    assert text[6:] == "World"
    assert text[::2] == "HloWrd"


def test_problem_2_methods():
    """Test string methods"""
    sentence = "python is awesome"
    assert sentence.upper() == "PYTHON IS AWESOME"
    assert sentence.capitalize() == "Python is awesome"
    assert sentence.replace('python', 'Python') == "Python is awesome"
    assert sentence.split() == ['python', 'is', 'awesome']


def test_problem_3_properties():
    """Test string properties"""
    text = "Hello123"
    assert 'ell' in text
    assert text.startswith('Hello')
    assert text.endswith('123')
    assert text.isalnum()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
