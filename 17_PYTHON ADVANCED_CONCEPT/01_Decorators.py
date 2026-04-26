# Decorators are a powerful tool in Python that allow you to modify the behavior of a function without changing its code. They are often used for logging, timing, and other cross-cutting concerns. Decoirators takes a function as an argument and returns a new function that can be used in place of the original function.

def logger(Func):
    def wrapper():
        print(f"Running {Func.__name__}")
        Func()
        print("Done")
    return wrapper

# def TwoSum():
#     print(2+3)
# f = logger(TwoSum)
# f()

# OR call like this
@logger
def Sum():
    print(2+4)
Sum()