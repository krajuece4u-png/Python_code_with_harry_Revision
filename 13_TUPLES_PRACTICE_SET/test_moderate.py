"""
Tests for 13_TUPLES - MODERATE PROBLEMS
Run with: pytest test_moderate.py -v
"""
import pytest


def test_problem_1_methods():
    """Test tuple methods"""
    numbers = (1, 2, 3, 2, 4, 2, 5)
    assert numbers.count(2) == 3
    assert numbers.index(3) == 2


def test_problem_2_operations():
    """Test tuple concatenation and repetition"""
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    combined = tuple1 + tuple2
    assert combined == (1, 2, 3, 4, 5, 6)
    
    repeated = tuple1 * 3
    assert repeated == (1, 2, 3, 1, 2, 3, 1, 2, 3)


def test_problem_3_nested():
    """Test nested tuples"""
    data = (("Alice", 25), ("Bob", 30), ("Charlie", 28))
    assert data[0] == ("Alice", 25)
    assert data[0][1] == 25
    
    for name, age in data:
        assert isinstance(name, str)
        assert isinstance(age, int)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
