from AssignmentOne.chapter7-ques07 import LinearEquation
x1,y1,x2,y2=eval(input("enter the end points of first line as x,y"))
x3,y3,x4,y4=eval(input("enter the end points of second line as x,y"))

a=-(y2-y1)/(x2-x3)
b=1
e=y1-(a*x1)

c=-(y3-y4)/(x3-x4)
d=1
f=y3-(c*x3)

LinearEquation=LinearEquation(a,b,c,d,e,f)
LinearEquation.getX()
LinearEquation.getY()