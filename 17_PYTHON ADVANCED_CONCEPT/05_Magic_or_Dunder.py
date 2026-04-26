# Magic or Dunder Methods in Python. 

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name of the emloyee is {self.name} and salary is {self.salary}"
    
    def __repr__(self):
        return f"name : {self.name}\nsalary : {self.salary}"
    
    def __len__(self):
        return len(self.name)
    
E1 = Employee("Raju", 345000)

print(E1.name)
print(str(E1))
print(repr(E1))
print(len(E1))