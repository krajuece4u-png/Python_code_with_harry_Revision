# Decorators with arguments and kwargs are a powerful tool in Python that allow you to modify the behavior of a function without changing its code. 
def repeat(n):
    def decorators(Func):
        def wrapper(a):
            for i in range(n):
                Func(a)
        return wrapper
    return decorators

@repeat(7)
def hello(a):
    print(f"Hello {a}")

hello("raju")



# If you want to create a decorator that can accept any number of arguments, you can use *args and **kwargs in the wrapper function. This allows the decorator to work with functions that have different numbers of arguments.
def decorators(Func):
    def wrapper(*args, **kwargs):
        Func(*args, **kwargs)               
    return wrapper


@decorators
def twoSum(a,b):
    print(f"sum = {a+b}")

twoSum(2,7)
    
 
    
 