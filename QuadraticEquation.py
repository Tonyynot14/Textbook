import math
class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c
    def getDiscriminate(self):
        discriminate = (self.__b**2)-(4*self.__a*self.__c)
        return discriminate
    def getRoot1(self):
        root1 = (-self.__b + (self.getDiscriminate()**(1/2)))/(2*self.__a)
        return root1
    def getRoot2(self):
        root2 = (-self.__b - (self.getDiscriminate()**(1/2)))/(2*self.__a)
        return root2

