"""
Tests for 11_FUNCTION - SIMPLE PROBLEMS
Run with: pytest test_simple.py -v
"""
import pytest


def test_problem_1_greet_function():
    """Test simple greeting function"""
    def greet(name):
        return f"Hello, {name}!"
    
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_problem_2_return_value():
    """Test function with return value"""
    def add(a, b):
        return a + b
    
    result = add(10, 20)
    assert result == 30


def test_problem_3_default_parameter():
    """Test function with default parameters"""
    def power(base, exp=2):
        return base ** exp
    
    assert power(2) == 4
    assert power(2, 3) == 8


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
