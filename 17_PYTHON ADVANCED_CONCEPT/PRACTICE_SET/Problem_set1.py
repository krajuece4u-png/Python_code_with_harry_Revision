# 1. Decorators in Python
# 1.1 Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!" .
def logger(Func):
    def wrapper():
        print(f"The function {Func.__name__} is beign called")
        Func()
    return wrapper()

@logger
def sayHello():
    print("Hello!")


# 1.2 Write a decorator timer that calculates how long a function takes to execute. Test it with a function that sums numbers from 1 to 1,000,000.
from time import time

def timmer(func):
    def wrapper(n):
        start_time = time()
        func(n)
        end_time = time()
        print(end_time - start_time)
    return wrapper

@timmer
def sum_all(n):
    total = 0
    for i in range(1,n+1):
        total += i
    return total

print(sum_all(1000000000)) 