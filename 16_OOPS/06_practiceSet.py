# 1. Create a Simple Class and Object
# Create a class Car with a method drive() that prints "Car is moving" .
# Create an object of Car and call drive() .


class car():
    def drive(self):
        print("Car is moving")

tata_sumo = car()
tata_sumo.drive()


# 2. Constructor and Attributes
# Create a class Person with a constructor ( __init__ ) that accepts name and age as arguments and stores them as instance attributes. Create an object and print the person’s name and age.

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age


Person1 = Person("Rahin",1)

print(Person1.name, Person1.age)
# # or 
# print(Person1.name)
# print(Person1.age)



# 3. Simple Inheritance
# Create a base class Animal with a method sound() that prints "Some sound" .
# Create a derived class Dog that overrides sound() to print "Bark!" .
# Create an object of Dog and call sound() .



class Animal():
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        # super().sound()  # This is the parent class method call
        print("Bark!")

D = Dog()
D.sound()