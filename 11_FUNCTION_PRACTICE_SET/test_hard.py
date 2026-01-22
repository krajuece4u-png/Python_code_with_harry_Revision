"""
Tests for 11_FUNCTION - HARD PROBLEMS
Run with: pytest test_hard.py -v
"""
import pytest


def test_problem_1_recursion():
    """Test recursive function"""
    def factorial(n):
        if n <= 1:
            return 1
        else:
            return n * factorial(n - 1)
    
    assert factorial(5) == 120
    assert factorial(6) == 720


def test_problem_2_lambda():
    """Test lambda functions"""
    square = lambda x: x ** 2
    add = lambda x, y: x + y
    
    assert square(5) == 25
    assert add(3, 7) == 10
    
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers))
    assert squared == [1, 4, 9, 16, 25]


def test_problem_3_docstring():
    """Test function with docstring"""
    def fibonacci(n):
        """
        Generate Fibonacci sequence up to n terms.
        """
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib[:n]
    
    result = fibonacci(7)
    assert result == [0, 1, 1, 2, 3, 5, 8]
    assert fibonacci.__doc__ is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
