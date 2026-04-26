# Error and Exception Handling in Python
# while True:
#         num1 = int(input("Enter the first number : "))
#         num2 = int(input("Enter the second number : "))
#         print(f"The sum of {num1} and {num2} is {num1 + num2}")

# The above code will give an error if the user enters a non-integer value. To handle this error, we can use try-except block.

while True:
    try:
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        print(f"The sum of {num1} and {num2} is {num1 / num2}")   

    #we can also specify the type of error we want to handle. For example, if we want to handle only ValueError, we can do it like this:

    except ValueError as e:
        print(f"Please enter a valid integer value.", "Error : ", e)
    
    except ZeroDivisionError as e:
        print(f"Cannot divide by zero.", "Error : ", e)

    except Exception as e:
        print(f"Internal server error.","error : ", e)