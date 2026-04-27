# 5. Exception Handling and Custom Errors
#     1. Write a program that asks the user to enter a number and handles:

#         1. ValueError if the input is not a number
#         1. ZeroDivisionError if you try to divide by zero
#     2. Create a custom exception NegativeNumberError and raise it when the user
#     enters a negative number.

class NegativeNumberError(Exception):
    pass

while  True:
    try:
        number1 = int(input("Enter your number1 : "))
        number2 = int(input("Enter your number2 : "))
         

        if number1 < 0:
            raise NegativeNumberError()
        else:
            result = number1/number2
            print("Result ", result)
        
    except ValueError as e:
        print("Please Enter a number", e)
    except ZeroDivisionError as e :
        print("Please Enter a non zero number", e)
    except NegativeNumberError as e:
        print("Negative number not allowed. ", e)
    except Exception as e:
        print("Some error occured")
    

    
    
    
