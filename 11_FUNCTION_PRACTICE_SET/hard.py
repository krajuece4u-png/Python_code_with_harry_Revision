"""
11_FUNCTION - HARD PROBLEMS
Recursion, lambda, and advanced function concepts.
"""

# PROBLEM 1: Recursion
# Create a recursive function to calculate factorial
print("=== PROBLEM 1 ===")
print("Recursive factorial function")
print()

# Solution:
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 6: {factorial(6)}")
print()

# PROBLEM 2: Lambda functions
# Use lambda for inline functions
print("=== PROBLEM 2 ===")
print("Lambda functions")
print()

# Solution:
square = lambda x: x ** 2
add = lambda x, y: x + y

print(f"Square of 5: {square(5)}")
print(f"Sum of 3 and 7: {add(3, 7)}")

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")
print()

# PROBLEM 3: Function documentation
# Create documented functions
print("=== PROBLEM 3 ===")
print("Function with docstring")
print()

# Solution:
def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms.
    Args: n - number of terms
    Returns: list of Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

print(f"Fibonacci sequence (7 terms): {fibonacci(7)}")
print(f"Docstring: {fibonacci.__doc__}")
