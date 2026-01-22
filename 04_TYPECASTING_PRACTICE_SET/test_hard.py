"""
Tests for 04_TYPECASTING - HARD PROBLEMS
Run with: pytest test_hard.py -v
"""
import pytest


def test_problem_1_chain_conversions():
    """Test chaining multiple type conversions"""
    value = "123"
    value = int(value)
    assert isinstance(value, int)
    value = float(value)
    assert isinstance(value, float)
    value = str(value)
    assert isinstance(value, str)
    assert value == "123.0"


def test_problem_2_safe_conversion():
    """Test safe type conversion with error handling"""
    def safe_int(val):
        try:
            return int(val)
        except ValueError:
            return None
    
    result1 = safe_int("100")
    result2 = safe_int("abc")
    assert result1 == 100
    assert result2 is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
