"""
Tests for 05_USER_INPUT - MODERATE PROBLEMS
Run with: pytest test_moderate.py -v
"""
import pytest


def test_problem_1_add_numbers():
    """Test adding two numbers from input"""
    def add_numbers(num1_str, num2_str):
        num1 = int(num1_str)
        num2 = int(num2_str)
        return num1 + num2
    
    result = add_numbers("20", "30")
    assert result == 50


def test_problem_2_rectangle_area():
    """Test calculating rectangle area from input"""
    def calculate_area(length_str, width_str):
        length = float(length_str)
        width = float(width_str)
        return length * width
    
    result = calculate_area("5.5", "3.2")
    assert result == pytest.approx(17.6)


def test_problem_3_student_average():
    """Test calculating student average"""
    def calculate_average(name, score1_str, score2_str, score3_str):
        score1 = float(score1_str)
        score2 = float(score2_str)
        score3 = float(score3_str)
        average = (score1 + score2 + score3) / 3
        return f"{name}'s average: {average}"
    
    result = calculate_average("Bob", "85", "90", "92")
    assert "Bob" in result
    assert "average" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
