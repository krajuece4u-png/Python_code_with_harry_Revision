"""
09_LOOPS - HARD PROBLEMS
Complex loop scenarios and nested structures.
"""

# PROBLEM 1: Prime numbers
# Find all prime numbers up to 20
print("=== PROBLEM 1 ===")
print("Find prime numbers from 1 to 20")
print()

# Solution:
primes = []
for num in range(2, 21):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print(f"Primes: {primes}")
print()

# PROBLEM 2: Create a 2D pattern
# Print a complex nested pattern
print("=== PROBLEM 2 ===")
print("2D pattern")
print()

# Solution:
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()
