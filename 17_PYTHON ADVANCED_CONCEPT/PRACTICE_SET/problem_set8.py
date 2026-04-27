# 8. *args and **kwargs
    # Write a function sum_all(*args) that accepts any number of integers and returns their sum.

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1,2,3,4,5))


    # Write a function print_details(**kwargs) that prints key-value pairs passed as arguments, for example:
    # print_details(name="Alice", age=25, city="Delhi")
        # Output:
        # name: Alice
        # age: 25
        # city: Delhi

def print_details(**kwargs):
    # for keys in kwargs:
    #     print(f"{keys} : {kwargs[keys]} ")

    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_details(name="Alice", age=25, city="Delhi")