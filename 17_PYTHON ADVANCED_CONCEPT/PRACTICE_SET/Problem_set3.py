# 3. Static & Class Methods

# 1. Create a class MathUtils with:
#     A @staticmethod called add(a, b) that returns a + b .
#     A @classmethod called description(cls) that prints "This is a utility class for math operations."

class MathUtils:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sumTwo(a,b):
        return a+b
    
    @classmethod
    def description(cls):
        print("This is a utility class for math operation")

M1 = MathUtils("Raju")

# Sum_result = M1.sumTwo(3,4)
# print(Sum_result)
# M1.description()
    
# 2. Call both methods without creating an object.

print(MathUtils("Raju").sumTwo(2,6))
MathUtils("Raju").description()
