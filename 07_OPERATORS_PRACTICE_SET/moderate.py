"""
07_OPERATORS - MODERATE PROBLEMS
Logical and comparison operators.
"""

# PROBLEM 1: Comparison operators
# Compare values and print results
print("=== PROBLEM 1 ===")
print("Comparison operators")
print()

# Solution:
a = 10
b = 20
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a < b: {a < b}")
print(f"a > b: {a > b}")
print(f"a <= b: {a <= b}")
print(f"a >= b: {a >= b}")
print()

# PROBLEM 2: Logical operators
# Use and, or, not operators
print("=== PROBLEM 2 ===")
print("Logical operators")
print()

# Solution:
x = 15
print(f"x > 10 and x < 20: {x > 10 and x < 20}")
print(f"x < 10 or x > 20: {x < 10 or x > 20}")
print(f"not (x > 20): {not (x > 20)}")
print()

# PROBLEM 3: Assignment operators
# Use compound assignment operators
print("=== PROBLEM 3 ===")
print("Assignment operators")
print()

# Solution:
num = 10
print(f"Initial: {num}")
num += 5
print(f"After += 5: {num}")
num -= 3
print(f"After -= 3: {num}")
num *= 2
print(f"After *= 2: {num}")
