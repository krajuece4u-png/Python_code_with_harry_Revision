"""
08_CONDITION - SIMPLE PROBLEMS
Basic if statements.
"""

# PROBLEM 1: Simple if statement
# Check if a number is positive
print("=== PROBLEM 1 ===")
print("Check if number is positive")
print()

# Solution:
num = 15
if num > 0:
    print(f"{num} is positive")
print()

# PROBLEM 2: If-else statement
# Check if number is even or odd
print("=== PROBLEM 2 ===")
print("Check if number is even or odd")
print()

# Solution:
num = 10
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
print()

# PROBLEM 3: Compare two numbers
# Find the larger number
print("=== PROBLEM 3 ===")
print("Find larger number")
print()

# Solution:
a = 25
b = 30
if a > b:
    print(f"{a} is larger")
else:
    print(f"{b} is larger")
