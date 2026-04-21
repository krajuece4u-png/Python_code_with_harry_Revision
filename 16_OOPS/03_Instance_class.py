class employee:

    company = "Google"  # Class Variable
    
    # Constructor
    def __init__(self, name, salary, role, company= company): # Default parameter for company
        self.name = name
        self.salary = salary
        self.role = role
        self.company = company

    # Instance Method
    def emp_details(self):
        return f"The salary of {self.name} is {self.salary} with role {self.role} in company {self.company}"

# Creating an object of the employee class    
emp1 = employee("Raju", 50000, "Developer", "Microsoft")
print(emp1.name)
print(e  mp1.company) # Accessing instance variable
print(employee.company)  # Accessing class variable
print(emp1.emp_details())


#object introspection
print(dir(emp1))  # Lists all attributes and methods of emp1 object