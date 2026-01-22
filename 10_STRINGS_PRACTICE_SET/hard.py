"""
10_STRINGS - HARD PROBLEMS
String formatting and complex manipulations.
"""

# PROBLEM 1: F-string formatting
# Use f-strings for complex formatting
print("=== PROBLEM 1 ===")
print("F-string formatting")
print()

# Solution:
name = "Alice"
score = 95.5
print(f"Student: {name}, Score: {score:.1f}%")
print(f"Score in uppercase: {name.upper()}")

data = {'x': 10, 'y': 20}
print(f"X={data['x']}, Y={data['y']}")
print()

# PROBLEM 2: String manipulation challenge
# Process and transform strings
print("=== PROBLEM 2 ===")
print("String manipulation")
print()

# Solution:
sentence = "  hello world from python  "
cleaned = sentence.strip().title()
print(f"Original: '{sentence}'")
print(f"Cleaned: '{cleaned}'")

# Count occurrences
text = "banana"
count = text.count('a')
print(f"Occurrences of 'a' in '{text}': {count}")
