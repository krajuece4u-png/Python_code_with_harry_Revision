Student = {"name": "John", "age": 21, "courses": ["Math", "CompSci"]}
print(Student, type(Student))

print(Student["name"])
print(Student["age"])
print(Student["courses"])

Student["age"] = 22  # Modifying an existing key-value pair
Student["phone"] = "555-5555"  # Adding a new key-value pair
print(Student)

print(Student.get("name")) # Using get() method
print(Student.get("address", "Kushmuri"))  # Using get() with a default value

print(Student.keys()) # Getting all keys
print(Student.values()) # Getting all values
print(Student.items()) # Getting all key-value pairs

print(len(Student)) # Getting the number of key-value pairs

# Iterating through the dictionary
for key in Student:
    print(key, ":", Student[key])

# Another way to iterate through the dictionary
for key, value in Student.items():
    print(key, "->", value)

# Removing key-value pairs
del Student["age"]
print(Student)

# Removing a specific key-value pair
Student.pop("phone")
print(Student)
