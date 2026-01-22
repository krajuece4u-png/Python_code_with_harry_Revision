"""
Tests for 09_LOOPS - HARD PROBLEMS
Run with: pytest test_hard.py -v
"""
import pytest


def test_problem_1_prime_numbers():
    """Test finding prime numbers"""
    primes = []
    for num in range(2, 21):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    
    assert len(primes) == 8
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19]


def test_problem_2_2d_pattern():
    """Test 2D pattern creation"""
    pattern = []
    for i in range(1, 6):
        row = []
        for j in range(1, 6):
            row.append(i * j)
        pattern.append(row)
    
    assert len(pattern) == 5
    assert pattern[0] == [1, 2, 3, 4, 5]
    assert pattern[4][4] == 25


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
