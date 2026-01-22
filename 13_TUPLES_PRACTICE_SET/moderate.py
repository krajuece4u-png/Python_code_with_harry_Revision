"""
13_TUPLES - MODERATE PROBLEMS
Tuple operations and methods.
"""

# PROBLEM 1: Tuple methods
# Use tuple methods
print("=== PROBLEM 1 ===")
print("Tuple methods")
print()

# Solution:
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Tuple: {numbers}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")
print()

# PROBLEM 2: Tuple concatenation and repetition
# Combine and repeat tuples
print("=== PROBLEM 2 ===")
print("Tuple operations")
print()

# Solution:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"Combined: {combined}")

repeated = tuple1 * 3
print(f"Repeated 3 times: {repeated}")
print()

# PROBLEM 3: Nested tuples
# Work with tuples containing other tuples
print("=== PROBLEM 3 ===")
print("Nested tuples")
print()

# Solution:
data = (("Alice", 25), ("Bob", 30), ("Charlie", 28))
print(f"Data: {data}")
print(f"First person: {data[0]}")
print(f"First person's age: {data[0][1]}")

for name, age in data:
    print(f"{name} is {age} years old")
