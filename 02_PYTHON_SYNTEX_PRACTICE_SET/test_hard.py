"""
Tests for 02_PYTHON_SYNTEX - HARD PROBLEMS
Run with: pytest test_hard.py -v
"""
import pytest


def test_problem_1_nested_structures():
    """Test nested structures with proper syntax"""
    data = {
        'name': 'John',
        'scores': [85, 90, 78],
        'details': {
            'age': 25,
            'city': 'New York'
        }
    }
    assert data['name'] == 'John'
    assert data['details']['age'] == 25
    assert len(data['scores']) == 3


def test_problem_2_complex_expression():
    """Test complex multi-line expression"""
    result = (
        10 * 5 +
        20 * 3 -
        15 / 3 +
        8 ** 2
    )
    assert result == 50 + 60 - 5 + 64
    assert result == 169


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
