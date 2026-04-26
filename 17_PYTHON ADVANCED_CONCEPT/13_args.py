# *args and **kwargs in Python
# *args and **kwargs are special syntax in Python that allow you to pass a variable number of arguments to a function.


# def sum_all(a,b):
#     return a+b

# result = sum_all(1,2,3) # error :Remove 1 unexpected arguments; 'sum_all' expects 2 positional arguments.
# print(result)



# To fix this error, we can use *args to allow the function to accept a variable number of arguments. The *args syntax allows us to pass a variable number of non-keyword arguments to a function. The arguments are passed as a tuple.
def sum_all(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    return total

result = sum_all(1,2,3,4,5,6,7,8,9,10)
print(result)