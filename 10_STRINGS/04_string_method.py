name = " kaji raju "  # String are immutable

# name[0] = "R" # You can not do this 

a = len(name)
print(a)
print(name.upper())

name = name.upper()
print(name)

text = " Python is fun "

print(text.strip())   #  "Python is fun"
print(text.lstrip())  # "Python is fun "
print(text.rstrip())  # " Python is fun"

print(text.find("is")) #Output: 7
print(text.replace("fun", "awsome"))


text_1 = "Apple, Bananas, Pineapples"

print(text_1.split(","))
print(",".join(['Apple', ' Bananas', ' Pineapples']))

text_2 = "Python123"

print(text_2.isalpha()) # Output: False
print(text_2.isdigit()) # Output: False
print(text_2.isalnum()) # Output: True
print(text_2.isspace()) # Output: False
print(text_2.isdecimal()) # Output: False
print(text_2.isupper()) # Output: False




