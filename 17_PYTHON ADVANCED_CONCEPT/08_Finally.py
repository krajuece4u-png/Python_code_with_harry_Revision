# Exception Handling with Finally block

while True:
    try:
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        print(f"The sum of {num1} and {num2} is {num1 / num2}") 

    except Exception as e:
        print("Some error occured please try with different input", "error:", e)


    finally:
        print("This block will always execute whether there is an error or not. It is used to perform cleanup actions like closing files, releasing resources, etc.")


# without finally by only using print statement it will still print the message even if there is an error. BBut inside the function it will not print the message if there is an error. So, to handle this situation we can use finally block.

def divide(num1, num2):
    try:
        print(f"The sum of {num1} and {num2} is {num1 / num2}") 
        return num1 / num2

    except Exception as e:
        print("Some error occured please try with different input", "error:", e)
        return None

    finally:
        print("This block will always execute whether there is an error or not. It is used to perform cleanup actions like closing files, releasing resources, etc.")
  
divide(10, 0)