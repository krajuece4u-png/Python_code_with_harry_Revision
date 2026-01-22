"""
13_TUPLES - HARD PROBLEMS
Advanced tuple concepts and applications.
"""

# PROBLEM 1: Tuples as dictionary keys
# Use tuples as keys in dictionaries
print("=== PROBLEM 1 ===")
print("Tuples as dictionary keys")
print()

# Solution:
coordinates = {
    (0, 0): "origin",
    (1, 0): "positive x",
    (0, 1): "positive y",
    (1, 1): "first quadrant"
}
print(f"Coordinates: {coordinates}")
print(f"Value at (1, 1): {coordinates[(1, 1)]}")
print()

# PROBLEM 2: Named tuples
# Create and use named tuples
print("=== PROBLEM 2 ===")
print("Named tuples")
print()

# Solution:
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)
print(f"Point: {p1}")
print(f"X coordinate: {p1.x}")
print(f"Y coordinate: {p1.y}")
print()

# PROBLEM 3: Tuple packing and unpacking with *
# Advanced unpacking techniques
print("=== PROBLEM 3 ===")
print("Advanced unpacking")
print()

# Solution:
data = (1, 2, 3, 4, 5)
first, *middle, last = data
print(f"First: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}")
