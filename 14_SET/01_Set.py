num = {12,4,5,6,74,995,23}

print(type(num))
# print(num[3])  # This will raise an error since sets do not support indexing

# Adding an element to the set
num.add(231)  # 231 will be added to the set
num.add(4)    # 4 is already in the set, so no change will occur
num.add((1,2,3))  # Adding a tuple to the set
print(num)
num.remove(74)  # Removes 74 from the set
# num.remove(100)  # This will raise an error since 100 is not in the set
num.discard(100)  # This will not raise an error even if 100 is not in the set
print(num)