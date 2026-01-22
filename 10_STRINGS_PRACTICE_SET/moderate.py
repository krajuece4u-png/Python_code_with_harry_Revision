"""
10_STRINGS - MODERATE PROBLEMS
String slicing and methods.
"""

# PROBLEM 1: String slicing
# Extract substrings using slicing
print("=== PROBLEM 1 ===")
print("String slicing")
print()

# Solution:
text = "Hello World"
print(f"First 5 chars: {text[:5]}")
print(f"Last 5 chars: {text[-5:]}")
print(f"Middle part: {text[6:]}")
print(f"Every 2nd char: {text[::2]}")
print()

# PROBLEM 2: String methods
# Use common string methods
print("=== PROBLEM 2 ===")
print("String methods")
print()

# Solution:
sentence = "python is awesome"
print(f"Uppercase: {sentence.upper()}")
print(f"Capitalize: {sentence.capitalize()}")
print(f"Replace: {sentence.replace('python', 'Python')}")
print(f"Split: {sentence.split()}")
print()

# PROBLEM 3: Check string properties
# Check if string contains specific patterns
print("=== PROBLEM 3 ===")
print("String properties")
print()

# Solution:
text = "Hello123"
print(f"Contains 'ell': {'ell' in text}")
print(f"Starts with 'Hello': {text.startswith('Hello')}")
print(f"Ends with '123': {text.endswith('123')}")
print(f"Is alphanumeric: {text.isalnum()}")
