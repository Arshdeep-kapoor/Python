class Point(object):

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y

    def distance(self, p2):
        return (((p2.getX() - self.getX())**2) + ((p2.getY() - self.getY())**2))**0.5
    
    def isNearBy(self, p2):
        if self.distance(p2)<5:
            return True
        else:
            return False
        
    def __str__(self):
        return (self.getX(),self.getY())

def main():
    
    x1,y1,x2,y2=eval(input("Enter the two points x1, y1, x2, y2 :"))
    p1 = Point(x1,y1)
    p2 = Point(x2,y2)
    print("The distance between the two points is ",p1.distance(p2))
    if (p1.isNearBy(p2)):
        print("The two points are near each other")
    else:
        print("The two points are not near each other")
    
main()