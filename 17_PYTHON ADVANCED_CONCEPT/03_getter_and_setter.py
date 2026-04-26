class Student:
    def __init__(self, name):
        self.name = name   # private variable
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

S = Student("Rahul")
print(S.get_name())   # getter

S.set_name("JESMIN")
print(S.get_name())    


# class Employee:
#     def __init__(self, name, salary):
#         self.name   = name 
#         self.salary = salary

#     @property
#     def first_name(self):
#         l = self.name.split(" ")
#         return self.name    
    
#     @first_name.setter
#     def first_name(self,name):
#         l = self.name.split(" ")
#         self.name = f"{name} {l[1]}"
#         return self.name
    
# E1 = Employee("Kaji Rahin", 409586)
# S = E1.first_name
# print(S)
# E1.first_name = "kazi"
# print(E1.name)


# 1. Simple Student Name
# Create a class Student:
# private variable: __name
# setter: set_name(name)
# getter: get_name()
# 👉 Task: Set name to "Rahul" and print it using getter.
# class Student:
#     def __init__(self, name):
#         self.name = name
    
#     @property
#     def full_name(self):
#         return self.name
    
#     @full_name.setter
#     def full_name(self, name):
#         self.name = name
#         return self.name

# S = Student("Kaji Raju")
# p1 = S.full_name
# print(p1)
# S.full_name = "Jesmin Begam"
# print(S.name)

