"""
Tests for 08_CONDITION - HARD PROBLEMS
Run with: pytest test_hard.py -v
"""
import pytest


def test_problem_1_triangle_validation():
    """Test triangle validation"""
    def validate_triangle(a, b, c):
        if a + b > c and b + c > a and a + c > b:
            if a == b == c:
                return "Equilateral"
            elif a == b or b == c or a == c:
                return "Isosceles"
            else:
                return "Scalene"
        return "Invalid"
    
    assert validate_triangle(3, 4, 5) == "Scalene"
    assert validate_triangle(5, 5, 5) == "Equilateral"
    assert validate_triangle(5, 5, 8) == "Isosceles"
    assert validate_triangle(1, 2, 5) == "Invalid"


def test_problem_2_number_classification():
    """Test complex number classification"""
    num = 17
    if num > 0:
        if num % 2 == 0:
            if num % 4 == 0:
                result = "positive, even, divisible by 4"
            else:
                result = "positive and even"
        else:
            result = "positive and odd"
    else:
        result = "not positive"
    assert "positive and odd" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
