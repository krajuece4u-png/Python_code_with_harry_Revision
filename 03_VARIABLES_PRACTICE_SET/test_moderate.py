"""
Tests for 03_VARIABLES - MODERATE PROBLEMS
Run with: pytest test_moderate.py -v
"""
import pytest


def test_problem_1_rectangle_area():
    """Test calculating rectangle area"""
    length = 10
    width = 5
    area = length * width
    assert area == 50


def test_problem_2_average_score():
    """Test calculating average of scores"""
    score1 = 85
    score2 = 90
    score3 = 78
    average = (score1 + score2 + score3) / 3
    assert average == pytest.approx(84.33, 0.01)


def test_problem_3_naming_conventions():
    """Test proper variable naming"""
    student_name = "Bob"
    student_age = 20
    is_active = True
    total_marks = 450
    assert student_name == "Bob"
    assert student_age == 20
    assert is_active is True
    assert total_marks == 450


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
