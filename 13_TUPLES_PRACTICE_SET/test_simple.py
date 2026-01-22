"""
Tests for 13_TUPLES - SIMPLE PROBLEMS
Run with: pytest test_simple.py -v
"""
import pytest


def test_problem_1_tuple_creation():
    """Test tuple creation and access"""
    colors = ("red", "green", "blue")
    assert len(colors) == 3
    assert colors[0] == "red"
    assert colors[-1] == "blue"


def test_problem_2_unpacking():
    """Test tuple unpacking"""
    person = ("Alice", 25, "NYC")
    name, age, city = person
    assert name == "Alice"
    assert age == 25
    assert city == "NYC"


def test_problem_3_immutability():
    """Test tuple immutability"""
    nums = (1, 2, 3)
    with pytest.raises(TypeError):
        nums[0] = 10


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
