# List methods 
marks = [78, 56, 69, 90]
extra_marks = [90,47]

marks.append(85)  # Adds 85 at the end of the list
print("After append:", marks)
marks.insert(2, 60)  # Inserts 60 at index 2
print("After insert:", marks)
marks.pop() #Remove the last element of the list
print("After pop / remove:", marks)
marks.extend(extra_marks) #extend the list by adding elements from extra_marks
print("After extend:", marks)
marks.remove(69) #Remove the first occurrence of 69
print("After remove 69:", marks)
marks.sort() #Sort the list in ascending order
print("After sort:", marks)
marks.reverse() #Reverse the order of the list
print("After reverse:", marks)
index_of_90 = marks.index(90) #Get the index of the first occurrence of 90
print("Index of 90:", index_of_90)
count_of_90 = marks.count(90) #Count how many times 90 appears in the list
print("Count of 90:", count_of_90)
marks.clear() #Remove all elements from the list
print("After clear:", marks)
# Output:
# After append: [78, 56, 69, 90, 85]
# After insert: [78, 56, 60, 69, 90, 85]
# After pop / remove: [78, 56, 60, 69, 90]
# After extend: [78, 56, 60, 69, 90, 90, 47]
# After remove 69: [78, 56, 60, 90, 90, 47]
# After sort: [47, 56, 60, 78, 90, 90]
# After reverse: [90, 90, 78, 60, 56, 47]
# Index of 90: 0
# Count of 90: 2
# After clear: []
