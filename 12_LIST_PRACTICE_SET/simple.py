"""
12_LIST - SIMPLE PROBLEMS
Basic list operations.
"""

# PROBLEM 1: Create and print a list
# Create a list and print all elements
print("=== PROBLEM 1 ===")
print("Create and print list")
print()

# Solution:
fruits = ["apple", "banana", "orange"]
print(fruits)
for fruit in fruits:
    print(fruit)
print()

# PROBLEM 2: List indexing
# Access list elements by index
print("=== PROBLEM 2 ===")
print("List indexing")
print()

# Solution:
numbers = [10, 20, 30, 40, 50]
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print(f"Element at index 2: {numbers[2]}")
print()

# PROBLEM 3: List slicing
# Extract sublists using slicing
print("=== PROBLEM 3 ===")
print("List slicing")
print()

# Solution:
items = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"First 3 items: {items[:3]}")
print(f"Last 2 items: {items[-2:]}")
print(f"Middle items: {items[2:5]}")
