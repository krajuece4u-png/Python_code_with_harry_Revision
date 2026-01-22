"""
12_LIST - HARD PROBLEMS
Advanced list operations and nested lists.
"""

# PROBLEM 1: Nested lists
# Work with lists containing other lists
print("=== PROBLEM 1 ===")
print("Nested lists operations")
print()

# Solution:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matrix: {matrix}")
print(f"Element at [1][2]: {matrix[1][2]}")

# Flatten the matrix
flat = [item for row in matrix for item in row]
print(f"Flattened: {flat}")
print()

# PROBLEM 2: Advanced list operations
# Complex filtering and transformations
print("=== PROBLEM 2 ===")
print("Advanced list operations")
print()

# Solution:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter and transform
result = [x**2 for x in numbers if x % 2 == 0]
print(f"Squares of even numbers: {result}")

# Using map and filter
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled numbers: {doubled}")
