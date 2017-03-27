import math
class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
        
    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c
    def getD(self):
        return self.__d
    def getE(self):
        return self.__e
    def getF(self):
        return self.__f
    
    def isSolvable(self):
        if ((self.__a*self.__d)-(self.__b*self.__c))==0:
            return True
    
    def getX(self):
        if self.isSolvable():
            print("The equation has no solution")
        else:
            print (((self.__e*self.__d)-(self.__b*self.__f))/((self.__a*self.__d)-(self.__b*self.__c)))

    def getY(self):
        if self.isSolvable():
            print("The equation has no solution") 
        else:
            result = (((self.__a*self.__f)-(self.__e*self.__c))/((self.__a*self.__d)-(self.__b*self.__c)))
            print(result)
               

a = eval(input("enter the value of a"))
b = eval(input("enter the value of b"))
c = eval(input("enter the value of c"))
d = eval(input("enter the value of d"))
e = eval(input("enter the value of e"))
f = eval(input("enter the value of f"))

LinearEquation=LinearEquation(a,b,c,d,e,f)

LinearEquation.getX()
LinearEquation.getY()