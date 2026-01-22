"""
07_OPERATORS - HARD PROBLEMS
Complex operator combinations and precedence.
"""

# PROBLEM 1: Operator precedence
# Demonstrate operator precedence in complex expressions
print("=== PROBLEM 1 ===")
print("Operator precedence")
print()

# Solution:
result1 = 2 + 3 * 4 - 5
result2 = (2 + 3) * (4 - 5)
result3 = 2 + 3 * 4 ** 2 - 5
print(f"2 + 3 * 4 - 5 = {result1}")
print(f"(2 + 3) * (4 - 5) = {result2}")
print(f"2 + 3 * 4 ** 2 - 5 = {result3}")
print()

# PROBLEM 2: Complex logical conditions
# Combine multiple conditions
print("=== PROBLEM 2 ===")
print("Complex logical conditions")
print()

# Solution:
age = 25
income = 50000
has_credit = True
approved = (age >= 18) and (income >= 30000) and (has_credit)
print(f"Loan approved: {approved}")

# Another example
score = 75
attendance = 85
passed = (score >= 60) and (attendance >= 80)
print(f"Exam passed: {passed}")
