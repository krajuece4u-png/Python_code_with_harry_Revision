# 2. Getters and Setters.

#2.1 Create a class Employee with a private attribute _salary .
#     Use @property to define a getter for salary .
#     Use @salary.setter to prevent setting negative values (print a warning   instead).
# 3.3 Create an object and test by setting positive and negative salaries.

class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary
    
    @salary.setter    
    def salary(self, value):
        if value < 0:
            print("Salary must be getter  than 0")
        else:
            self._salary = value
            


E1 = Employee(54000)
print(E1.salary)
E1.salary = -100000
print("updated salary = ", E1.salary)
E1.salary = 100000
print("updated salary = ",E1.salary)



        

