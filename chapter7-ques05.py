import math
class regularPolygon:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n=n
        self.__side=side
        self.__x=x
        self.__y=y
    def getNumberOfSides(self):
        return self.__n
    def getLength(self):
        return self.__side
    def getXcordinate(self):
        return self.__x
    def getYcordinate(self):
        return self.__y
    def setNumberOfSides(self,n):
        self.__n = n
        return self.__n
    def setLength(self,side):
        self.__side = side
        return self.__side
    def setXcordinate(self,x):
        self.__x=x
        return self.__x
    def setYcordinate(self,y):
        self.__y = y
        return self.__y
    
    def getPerimeter(self):
        return (self.__n * self.__side)
    def getArea(self):
        return ((self.__n*self.__side*self.__side)/(4*math.tan(math.pi/self.__n)))
    
RegularPolygon=regularPolygon(6,4)
print("The perimeter is",RegularPolygon.getPerimeter())
print("the area is",RegularPolygon.getArea())


RegularPolygon=regularPolygon(10,4,5.6,7.8)
print("The perimeter is",RegularPolygon.getPerimeter())
print("the area is",RegularPolygon.getArea())