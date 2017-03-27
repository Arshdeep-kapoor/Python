from GeometricObject import GeometricObject
class Triangle(GeometricObject):
    def __init__(self,side1=1,side2=1,side3=1):
        super().__init__()
        self.__side1=side1
        self.__side2=side2
        self.__side3=side3
        
    def getSide1(self):
        return self.__side1
    
    def getSide2(self):
        return self.__side2
    
    def getSide3(self):
        return self.__side3
    
    def getArea(self):
        s=(self.__side1+self.__side2+self.__side3)/2
        return pow((s*(s-self.__side1)*(s-self.__side2)*(s-self.__side3)),0.5)
    
    def getPerimeter(self):
        return (self.__side1+self.__side2+self.__side3)
    
    def __str__(self):
        return super().__str__()+"Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 = " + str(self.__side3)
    
s1,s2,s3=eval(input("enter the three sides of the triangle"))
color=input("enter the color ")
fill=eval(input("1 or 0 to indicate whether the triangle"))
T1=Triangle(s1,s2,s3)
T1.setColor(color)
if fill==0:
    T1.setFilled(False)
print("The area is",T1.getArea())
print("The perimeter is",T1.getPerimeter())
print("A triangle is",T1.getColor())
print("if triangle is filled",T1.isFilled())

