a = 67
b = "56"

print("Type of a before:", type(a))
print("Type of b before:", type(b))

c = str(a)  # Typecasting integer to string
d = int(b)  # Typecasting string to integer

print("Type of c after typecasting a to string:", type(c))
print("Type of d after typecasting b to integer:", type(d))

print("Type of a after:", type(a))
print("Type of b after:", type(b))


# Additional examples of typecasting
pi = 3.14
f = int(pi)  # Typecasting float to integer
print("Type of f after typecasting pi to integer:", type(f))


g = float(b)  # Typecasting string to float
print("Type of g after typecasting b to float:", type(g))

bool_var = bool('0')  # Typecasting integer to boolean
print("Type of bool_var after typecasting '0' to boolean:", type(bool_var))