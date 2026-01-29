class employee:
    
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def get_salary(self):
        return f"The salary of {self.name} is {self.salary} with role {self.role}"
    
emp1 = employee("Raju", 50000, "Developer")
print(emp1.name)
print(emp1.get_salary())