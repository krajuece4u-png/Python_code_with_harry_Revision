"""
12_LIST - MODERATE PROBLEMS
List methods and manipulations.
"""

# PROBLEM 1: List methods
# Use common list methods
print("=== PROBLEM 1 ===")
print("List methods")
print()

# Solution:
nums = [3, 1, 4, 1, 5, 9]
print(f"Original: {nums}")

nums.append(2)
print(f"After append(2): {nums}")

nums.remove(1)
print(f"After remove(1): {nums}")

nums.sort()
print(f"After sort(): {nums}")

nums.reverse()
print(f"After reverse(): {nums}")
print()

# PROBLEM 2: List comprehension
# Create lists using comprehension
print("=== PROBLEM 2 ===")
print("List comprehension")
print()

# Solution:
squares = [x**2 for x in range(1, 6)]
print(f"Squares 1-5: {squares}")

evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers 1-10: {evens}")
print()

# PROBLEM 3: Combine lists
# Merge and extend lists
print("=== PROBLEM 3 ===")
print("Combine lists")
print()

# Solution:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"Combined: {combined}")

list1.extend([7, 8])
print(f"After extend: {list1}")
