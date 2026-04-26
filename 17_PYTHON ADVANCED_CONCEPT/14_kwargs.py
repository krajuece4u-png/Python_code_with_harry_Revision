# **kwargs in Python
# **kwargs allows you to pass a variable number of keyword arguments to a function. The arguments are passed as a dictionary.

def print_info(**kwargs):
    print(kwargs)
    print(kwargs.items())
    print(kwargs.keys())
    print(kwargs.values())

    for key, value in kwargs.items():
        print(f"{key}: {value}")

    for key in kwargs.keys():
        print(f"The {key}: {kwargs[key]}")


print_info(name="John", age=30, city="New York")