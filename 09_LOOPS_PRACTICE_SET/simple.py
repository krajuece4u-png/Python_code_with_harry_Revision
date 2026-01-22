"""
09_LOOPS - SIMPLE PROBLEMS
Basic for and while loops.
"""

# PROBLEM 1: Print numbers 1 to 5
# Use for loop to print numbers
print("=== PROBLEM 1 ===")
print("Print numbers 1 to 5 using for loop")
print()

# Solution:
for i in range(1, 6):
    print(i, end=" ")
print("\n")

# PROBLEM 2: Print table of 5
# Print multiplication table for 5
print("=== PROBLEM 2 ===")
print("Multiplication table of 5")
print()

# Solution:
for i in range(1, 11):
    print(f"5 × {i} = {5 * i}")
print()

# PROBLEM 3: Sum of numbers
# Calculate sum using while loop
print("=== PROBLEM 3 ===")
print("Sum of numbers 1 to 10")
print()

# Solution:
total = 0
n = 1
while n <= 10:
    total += n
    n += 1
print(f"Sum: {total}")
