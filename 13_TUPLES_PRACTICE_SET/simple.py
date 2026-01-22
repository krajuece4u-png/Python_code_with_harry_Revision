"""
13_TUPLES - SIMPLE PROBLEMS
Basic tuple operations.
"""

# PROBLEM 1: Create and print tuples
# Create tuples and access elements
print("=== PROBLEM 1 ===")
print("Create and print tuples")
print()

# Solution:
colors = ("red", "green", "blue")
print(colors)
print(f"First color: {colors[0]}")
print(f"Last color: {colors[-1]}")
print()

# PROBLEM 2: Tuple unpacking
# Unpack tuple values to variables
print("=== PROBLEM 2 ===")
print("Tuple unpacking")
print()

# Solution:
person = ("Alice", 25, "NYC")
name, age, city = person
print(f"Name: {name}, Age: {age}, City: {city}")
print()

# PROBLEM 3: Tuple immutability
# Demonstrate that tuples are immutable
print("=== PROBLEM 3 ===")
print("Tuple immutability")
print()

# Solution:
nums = (1, 2, 3)
print(f"Tuple: {nums}")
try:
    nums[0] = 10  # This will cause an error
except TypeError as e:
    print(f"Error: Cannot modify tuple - {e}")
