"""
08_CONDITION - HARD PROBLEMS
Nested conditions and complex logic.
"""

# PROBLEM 1: Triangle validation
# Check if three sides can form a triangle
print("=== PROBLEM 1 ===")
print("Triangle validation")
print()

# Solution:
a, b, c = 3, 4, 5
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Not a valid triangle")
print()

# PROBLEM 2: Number classification
# Complex number classification
print("=== PROBLEM 2 ===")
print("Complex number classification")
print()

# Solution:
num = 17
if num > 0:
    if num % 2 == 0:
        if num % 4 == 0:
            print(f"{num} is positive, even, and divisible by 4")
        else:
            print(f"{num} is positive and even")
    else:
        print(f"{num} is positive and odd")
else:
    print(f"{num} is not positive")
