"""
06_COMMENT_ESCAPE_PRINT - MODERATE PROBLEMS
Multi-line comments and complex escape sequences.
"""

# PROBLEM 1: Use multi-line strings as documentation
# Create a function with multi-line documentation
print("=== PROBLEM 1 ===")
print("Multi-line documentation")
print()

# Solution:
def add(a, b):
    '''
    This function adds two numbers
    Parameters: a, b (numbers)
    Returns: sum of a and b
    '''
    return a + b

result = add(5, 10)
print(f"Sum: {result}")
print()

# PROBLEM 2: Complex escape sequences
# Print formatted output with various escape sequences
print("=== PROBLEM 2 ===")
print("Complex escape sequences")
print()

# Solution:
print("Line 1\\nLine 2\\nLine 3")
print("Column1\\tColumn2\\tColumn3")
print("Quote: \\'Hello\\'")
print()

# PROBLEM 3: Print formatted table
# Print a table with proper alignment
print("=== PROBLEM 3 ===")
print("Formatted table")
print()

# Solution:
print("Name\\tAge\\tCity")
print("---\\t---\\t---")
print("John\\t25\\tNY")
print("Jane\\t30\\tLA")
