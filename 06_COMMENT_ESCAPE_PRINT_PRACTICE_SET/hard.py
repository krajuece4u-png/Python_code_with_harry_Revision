"""
06_COMMENT_ESCAPE_PRINT - HARD PROBLEMS
Advanced print formatting and special characters.
"""

# PROBLEM 1: Create formatted ASCII table
# Design and print an ASCII table with borders
print("=== PROBLEM 1 ===")
print("ASCII table with borders")
print()

# Solution:
print("+--------+-----+-------+")
print("| Name   | Age | Score |")
print("+--------+-----+-------+")
print("| Alice  |  25 |    95 |")
print("| Bob    |  23 |    87 |")
print("| Charlie|  26 |    92 |")
print("+--------+-----+-------+")
print()

# PROBLEM 2: Print with raw strings
# Use raw strings to handle special characters
print("=== PROBLEM 2 ===")
print("Raw strings and special characters")
print()

# Solution:
path = r"C:\\Users\\Name\\Documents"
print(f"Path: {path}")
regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
print(f"Regex: {regex}")
