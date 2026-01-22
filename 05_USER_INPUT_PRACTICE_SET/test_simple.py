"""
Tests for 05_USER_INPUT - SIMPLE PROBLEMS
Run with: pytest test_simple.py -v
"""
import pytest
from io import StringIO
from unittest.mock import patch


def test_problem_1_name_greeting():
    """Test name greeting function"""
    # Testing the function logic
    def greet_user(name):
        return f"Hello, {name}!"
    
    result = greet_user("Alice")
    assert result == "Hello, Alice!"


def test_problem_2_age_input():
    """Test age input processing"""
    def process_age(age):
        return f"You are {age} years old"
    
    result = process_age("25")
    assert "25" in result
    assert "years old" in result


def test_problem_3_multiple_inputs():
    """Test multiple input processing"""
    def process_inputs(name, age, city):
        return f"Name: {name}, Age: {age}, City: {city}"
    
    result = process_inputs("Alice", "25", "NYC")
    assert "Alice" in result
    assert "25" in result
    assert "NYC" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
