
# Global  Scope
def sum(a,b):
    c = a + b  # 'c' is a local variable
    global z
    z = 1   # 'z' is also a local variable
    return c

z = 5 
print(sum(5, 3))
print(z)
z = 5 
print(z)