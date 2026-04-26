# Filter function in python is used to filter out elements from an iterable (like list, tuple etc.) based on a condition. The syntax of the filter function is as follows:
# filter(function, iterable)

myList = [1,2,5,70,49,4,6]

def isEven(x):
    if x%2 ==0:
        return True
    else:
        return False
    
filterList = list(filter(isEven, myList))
print(filterList)