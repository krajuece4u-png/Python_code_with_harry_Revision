class Animal: #parent class(superclass)
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is speaking now...")

# Child class inheriting from Animal class     
class Dog(Animal): #child class(subclass)
    def speak(self):
        super().speak()  # Calling the parent class method
        print("Woof! Woof!")
    

a = Animal("Animal")
print(a.name) 
print(a.speak())

b = Dog("Tommy")
b.speak()
