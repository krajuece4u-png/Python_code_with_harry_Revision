# Walrus Operator in Python
# The walrus operator (:=) is a new operator in Python 3.8 that allows you to assign a value to a variable as part of an expression.

myList = [1,2,3,4,5,6,7,8,9,10
          ]
# Example without walrus operator
n = len(myList)
if n > 5:
    print(f"List has {n} elements")

# Example with walrus operator
if (n := len(myList)) > 5:
    print(f"List has {n} elements")
# In the above example, we are using the walrus operator to assign the value of len(myList) to the variable n and then checking if n is greater than 5 in the same expression. This can make our code more concise and easier to read.