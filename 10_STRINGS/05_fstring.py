# String Formating

template = " I am {}, a {} developer"

a = "Sima"
a1 = "java"

b = "Dinesh"
b1 = "JavaScript"

c = "Raju"
c1 = "Python"

s = template.format(b,b1)
s1 = template.format(a,a1)
print(s,'\n',s1)

print(f"I am {c}, a {c1} Developer")


