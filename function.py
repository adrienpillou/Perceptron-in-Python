# Author : Adrien Pillou
# Created : 10/09/2020

# This class is used to create an linear algebraic function : y(x) = ax+b.

class Function:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        pass

    def f(self, x):
        return self.a*x + self.b

    def GetxValue(self, y):
        if(self.a == 0):
            return 0
        return (y-self.b)/self.a
