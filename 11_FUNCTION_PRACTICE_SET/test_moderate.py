"""
Tests for 11_FUNCTION - MODERATE PROBLEMS
Run with: pytest test_moderate.py -v
"""
import pytest


def test_problem_1_multiple_parameters():
    """Test function with multiple parameters"""
    def calculate_grade(math, science, english):
        average = (math + science + english) / 3
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        else:
            return 'F'
    
    assert calculate_grade(85, 88, 92) == 'B'


def test_problem_2_args():
    """Test function with *args"""
    def sum_all(*numbers):
        total = 0
        for num in numbers:
            total += num
        return total
    
    assert sum_all(1, 2, 3) == 6
    assert sum_all(1, 2, 3, 4, 5) == 15


def test_problem_3_kwargs():
    """Test function with **kwargs"""
    def get_info(**info):
        return info
    
    result = get_info(name="Alice", age=25, city="NYC")
    assert result['name'] == "Alice"
    assert result['age'] == 25


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
