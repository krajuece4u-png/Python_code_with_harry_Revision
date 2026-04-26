# Reduce function in python is used to apply a function cumulatively to the items of an iterable (like list, tuple etc.), from left to right, so as to reduce the iterable to a single accumulated value. The syntax of the reduce function is as follows:
# reduce(function, iterable)

from functools import reduce

myList = [1,2,3,4,5,6,7,8,9,10]

# def two_sum(x,y):
#     return x+y

# print(reduce(two_sum, myList))
print(reduce(lambda x,y:x+y, myList)) # we can also use lambda function instead of defining a separate function. This will give us the same result as above.




