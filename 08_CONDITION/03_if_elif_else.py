age = int(input("Enter your age: "))

if age>=18:
    print("you can drive")
elif age==17:
    print("you can drive from next year")
elif age<=0:
    print("age can't be zero or negative")
else:
    print("You can't drive unit 18")

print("End of program")