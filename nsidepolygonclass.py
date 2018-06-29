#Tony Wade
# Class for regular polygons
# Class that defines a polygon based on n(number of sides), side(length of side)
# x(x coordinate) y(y coordinate)

import math

class RegularPolygon:
    # initalizer and default constructor of regular polygon
    def __init__(self, n=3, side = 1, x = 0, y = 0 ):
        self.__n= n
        self.__side = side
        self.__x = x
        self.__y = y
    # accessor function followed by mutator function of each piece of data
    def getN(self):

        return self.__n
    def setN(self,n):
        self.__n = n

    def getSide(self):
        return self.__side

    def setSide(self, side):
        self.__side = side

    def getX(self):
            return self.__x
    def setX(self, x):
            self.__x = x

    def getY(self):
        return self.__Y
    def setY(self, y):
        self.__y = y

    # Function for finding perimeter of regular sided polygon
    def getPerimeter(self):
        perimeter = self.__side*self.__n
        return perimeter
    # Function for finding the area of a regular sided polygon. Need math module for pi and tan functions.
    def getArea(self):
        area = (self.__n*(self.__side**2))/(4*math.tan(math.pi/self.__n))
        return area
