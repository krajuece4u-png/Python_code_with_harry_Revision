# List comprehension
marks = [78, 56, 69, 90]
# Create a new list with each mark increased by 5 using list comprehension
new_marks = [mark + 5 for mark in marks]
print("Original marks:", marks)
print("New marks:", new_marks)

# Create the table of squares from 1 to 10 using list comprehension
sqr_tbl = [x*x for x in range(1,11)]
print(sqr_tbl)