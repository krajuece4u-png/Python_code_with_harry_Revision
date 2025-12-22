n1 = input ("Enter first number: ")
n2 = input ("Enter second number: ")
sum = n1 + n2
print("The sum is: ", sum)  # This will concatenate the two inputs as strings if n1 =3 and n2=5, output will be 35

# To perform addition, we need to typecast the inputs to integers
sum = int(n1) +  int(n2)
print("The sum after typecasting is: ", sum)