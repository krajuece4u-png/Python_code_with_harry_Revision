# 6. map(), filter(), and reduce()
#     Use map() to convert [1, 2, 3, 4, 5] into their cubes.
#     Use filter() to get only even numbers from [10, 11, 12, 13, 14] .
#     Use reduce() from functools to find the product of all elements in [1, 2,3, 4] .


mylist = [1,2,3,4,5]
def qub(x):
    return x*x*x

# newList = list(map(qub,mylist))
newList = list(map(lambda x:x*x*x, mylist))
print(newList)


def EvenFn(x):
    if x%2 == 0:
        return True
    else:
        return False
    
FilterList = list(filter(EvenFn, mylist))
print(FilterList)   

from functools import reduce
ReduceValue = reduce(lambda x,y : x*y, mylist)
print(ReduceValue)