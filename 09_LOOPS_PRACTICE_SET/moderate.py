"""
09_LOOPS - MODERATE PROBLEMS
Nested loops, break, and continue.
"""

# PROBLEM 1: Print pattern with nested loops
# Create a pattern using nested for loops
print("=== PROBLEM 1 ===")
print("Print star pattern")
print()

# Solution:
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
print()

# PROBLEM 2: Find factorial using loop
# Calculate factorial of a number
print("=== PROBLEM 2 ===")
print("Calculate factorial")
print()

# Solution:
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of {n}: {factorial}")
print()

# PROBLEM 3: Use break and continue
# Skip and break in loops
print("=== PROBLEM 3 ===")
print("Break and continue examples")
print()

# Solution:
print("Break example:")
for i in range(1, 6):
    if i == 3:
        break
    print(i, end=" ")
print("\n")

print("Continue example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")
print()
