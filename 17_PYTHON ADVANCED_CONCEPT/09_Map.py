# Map function in python is used to apply a function to all the items in an iterable (like list, tuple etc.) and returns a map object (which is an iterator). The syntax of the map function is as follows:
# map(function, iterable)

myList = [1,2,5,70,49,4,6]

def square(x):
    return x*x

newList = list(map(square, myList))
print(newList)