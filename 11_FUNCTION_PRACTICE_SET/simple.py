"""
11_FUNCTION - SIMPLE PROBLEMS
Basic function definition and calls.
"""

# PROBLEM 1: Simple function
# Create a function that greets a user
print("=== PROBLEM 1 ===")
print("Simple greeting function")
print()

# Solution:
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
print()

# PROBLEM 2: Function with return
# Create a function that returns a value
print("=== PROBLEM 2 ===")
print("Function with return value")
print()

# Solution:
def add(a, b):
    return a + b

result = add(10, 20)
print(f"Sum: {result}")
print()

# PROBLEM 3: Function with default parameter
# Create a function with default values
print("=== PROBLEM 3 ===")
print("Function with default parameters")
print()

# Solution:
def power(base, exp=2):
    return base ** exp

print(f"2^2 = {power(2)}")
print(f"2^3 = {power(2, 3)}")
