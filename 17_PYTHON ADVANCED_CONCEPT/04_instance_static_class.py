class Employee:
    company = "TCS"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    #Instance method 
    def print_info(self):
        info = f" The name of the employee is {self.name} and the salary is {self.salary}"
        print(info)

    # Static Method
    @staticmethod
    def TwoSum(a,b):
        print(a+b)
    
    #class Method
    @classmethod
    def exmClassMethod(cls, newcompany):
        cls.company = newcompany
        return cls.company



E1 = Employee("raju", 45000)
print(E1.company)
E1.print_info()
E1.TwoSum(2,6)
a = E1.exmClassMethod("HP")
print(a)