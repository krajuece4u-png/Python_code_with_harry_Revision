# Slicing in Strings
name = "KAJIRAJU"

# name = "K  A  J  I  R  A  J  U"
#         0  1  2  3  4  5  6  7
#        -8 -7 -6 -5 -4 -3 -2 -1

#   Accessing characters using slicing

print(name[1:5])
print(name[:5])
print(name[2:])
print(name[-4:-1])
print(name[-4:])
print(name[:-4])
print(name[0:7:2])  # Step slicing
print(name[::3])    # Step slicing with default start and end
print(name[::-1])   # Reversing the string using slicing   
print(name[::-2])   # Reversing the string with step slicing
print(name[5:2:-1]) # Slicing with negative step