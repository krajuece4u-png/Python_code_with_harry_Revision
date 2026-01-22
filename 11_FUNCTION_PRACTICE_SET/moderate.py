"""
11_FUNCTION - MODERATE PROBLEMS
Functions with multiple parameters and variable arguments.
"""

# PROBLEM 1: Function with multiple parameters
# Create a function for complex calculations
print("=== PROBLEM 1 ===")
print("Function with multiple parameters")
print()

# Solution:
def calculate_grade(math, science, english):
    average = (math + science + english) / 3
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    else:
        return 'F'

grade = calculate_grade(85, 88, 92)
print(f"Grade: {grade}")
print()

# PROBLEM 2: Function with *args
# Function accepting variable number of arguments
print("=== PROBLEM 2 ===")
print("Function with variable arguments")
print()

# Solution:
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1,2,3: {sum_all(1, 2, 3)}")
print(f"Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")
print()

# PROBLEM 3: Function with **kwargs
# Function with keyword arguments
print("=== PROBLEM 3 ===")
print("Function with keyword arguments")
print()

# Solution:
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
