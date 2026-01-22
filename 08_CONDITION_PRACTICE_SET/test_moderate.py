"""
Tests for 08_CONDITION - MODERATE PROBLEMS
Run with: pytest test_moderate.py -v
"""
import pytest


def test_problem_1_grade_assignment():
    """Test grade assignment based on score"""
    def get_grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
    
    assert get_grade(85) == 'B'
    assert get_grade(92) == 'A'
    assert get_grade(75) == 'C'


def test_problem_2_age_classification():
    """Test age classification"""
    def classify_age(age):
        if age < 13:
            return "Child"
        elif age < 20:
            return "Teenager"
        elif age < 60:
            return "Adult"
        else:
            return "Senior"
    
    assert classify_age(10) == "Child"
    assert classify_age(15) == "Teenager"
    assert classify_age(35) == "Adult"
    assert classify_age(65) == "Senior"


def test_problem_3_discount_eligibility():
    """Test discount eligibility"""
    age = 65
    is_student = False
    if age < 12 or age >= 60:
        discount = True
    elif is_student:
        discount = True
    else:
        discount = False
    assert discount is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
