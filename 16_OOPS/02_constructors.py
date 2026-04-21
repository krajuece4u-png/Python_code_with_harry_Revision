# Constructor is a special method that is automatically called when an object of the class is created. It is used to initialize the attributes of the class.

class employee:
    def __init__(self, name, salary, role): # Constructor with parameters
        self.name = name
        self.salary = salary
        self.role = role
        
    # Instance Method
    def get_salary(self):
        return f"The salary of {self.name} is {self.salary} with role {self.role}"
    
emp1 = employee("Raju", 50000, "Developer")
print(emp1.name)
print(emp1.get_salary())