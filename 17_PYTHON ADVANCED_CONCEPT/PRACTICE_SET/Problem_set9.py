# # 9. Bonus Challenges
# #     1. Combine a decorator with *args and **kwargs support so it can wrap any
# #     function regardless of its parameters.
# def args_kwargs(func):
#     def wrapper(*args, **kwargs):
#         print(f"the args of this function is(if any) {args}")
#         print(f"The kwargs of this fuction  is(if any) {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper

# @args_kwargs
# def two_sum(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# a = two_sum(1,2,3,4,5)
# print(a)


# #     2. Implement __add__ in a Vector class so that adding two Vector objects
# #     returns a new Vector with summed components.

# class Point():
#     def __init__(self,p1,p2):
#         self.p1 = p1
#         self.p2 = p2

#     def __add__(self, p):
#         print(p[0],p[1])
#         return (p[0]+self.p1, p[1]+self.p2)
    
# P1 = Point(2,3)
# p=(4,6)
# result = P1.__add__(p)
# print(result)



#     3. Create a small program where invalid user input raises a custom exception,
#     logs the error, and continues execution instead of crashing.

class Custome_Exception(Exception):
    pass

while True:
    try:
        cus_input = int(input("Enter you number :"))
        if cus_input == 0:
            raise Custome_Exception("Please enter non zero number")
    except Custome_Exception as e: # Custome exception.
        print(f"error : {e}")
    except ValueError as e :  # In built exception.
        print(f"error :  {e}")