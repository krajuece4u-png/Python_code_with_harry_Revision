"""
08_CONDITION - MODERATE PROBLEMS
If-elif-else statements.
"""

# PROBLEM 1: Grade assignment
# Assign grade based on score
print("=== PROBLEM 1 ===")
print("Assign grade based on score")
print()

# Solution:
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Score: {score}, Grade: {grade}")
print()

# PROBLEM 2: Age classification
# Classify person by age
print("=== PROBLEM 2 ===")
print("Classify person by age")
print()

# Solution:
age = 15
if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"
print(f"Age: {age}, Category: {category}")
print()

# PROBLEM 3: Check eligibility
# Check if eligible for discount
print("=== PROBLEM 3 ===")
print("Check discount eligibility")
print()

# Solution:
age = 65
is_student = False
if age < 12 or age >= 60:
    print("You get a senior/child discount")
elif is_student:
    print("You get a student discount")
else:
    print("No discount applicable")
