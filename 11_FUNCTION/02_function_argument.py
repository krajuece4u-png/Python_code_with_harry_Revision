# Function with default parameter
def greet(name="Guest"):
    print("Hello, " + name)

greet("Raju")
greet()


# keyword arguments
def student(name, age):
    return f"Name: {name}, Age: {age}" 

text = student(age=25, name="Anita")
print(text)