class Point():

    def __init__(self,x,y):
        self.x = x 
        self.y = y

    def sumpoint(self, p):
        return Point((self.x +p.x), (self.y +p.y))
    

    def printfun(self):
        print(f"The value of x is {self.x} and the value of y is {self.y}")

    def __add__(self, p):
        return (f"The value of x is {self.x + p.x} and the value of y is {self.y + p.y}")


P1 = Point(2,8)
P2 = Point(9,5)

P = P1.sumpoint(P2)
P.printFun()

P = P1+P2
print(P)