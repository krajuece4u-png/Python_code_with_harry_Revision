# List are ordered, mutable(changeable), and allow duplicate elements.

marks = [78, 56, 69, 90]
mixed = [75, "raju", True]

print(type(marks))
print(marks[2])
print(mixed[1])
print(marks[-1])
print(mixed[-2])
print(marks[1:3])
print(mixed[0:2])
print(marks[:2])
print(mixed[1:])
print(marks[::2])
print("hello", mixed[::-1])
print(marks[4])# IndexError: list index out of range
