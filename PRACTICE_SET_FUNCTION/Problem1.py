# Maximum of Two Numbers, Write a function that returns the larger of two numbers.

def larger_num(num1,num2):
    first_num  = (num1*10)+num2
    second_num = (num2*10)+num1
    return(max(first_num,second_num))


result = larger_num(3,7)  
print(result)


# Intermediate (Medium)

# Factorial Function
# Write a function to calculate the factorial of a number.

def factorial(num):
    if(num>0):
        return (num-1)*factorial(num)

    return result

print(factorial(5))

# Palindrome Check
# Create a function that checks whether a string is a palindrome.

# Prime Number Check
# Write a function that returns True if a number is prime, otherwise False.

# Count Vowels
# Create a function that counts the number of vowels in a string.

# Sum of List Elements
# Write a function that takes a list and returns the sum of all elements.