# Exception Handling with else block

while True:
    try:
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        print(f"The sum of {num1} and {num2} is {num1 / num2}")    

    except Exception as e:
        print("Internal server error.","error : ", e)

    else:
        print("The operation was successful. There are no errors in the code.")