#class : A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.

#Object: An object is an instance of a class. It is created using the class blueprint and can have its own unique values for the attributes defined in the class.

class Employee:
    #class attributes
    company = "Google"
    salary = 100

    #class method
    def get_salary(self):
        return 26388

#creating objects
emp1 = Employee()
emp2 = Employee()

print(emp1.get_salary())  # Employee get salary method is calling here
print(emp1.salary)      # Employee class attribute salary is calling here
print(emp2.company)     # Employee class attribute company is calling here