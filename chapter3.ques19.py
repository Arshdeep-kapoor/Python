import turtle
import math

x1,y1 = eval(input("enter the coordinates of first point"))
x2,y2 = eval(input("enter the coordinates of second number"))

turtle.penup()
turtle.goto(x1,y1)
turtle.write(str(x1)+","+str(y1))
turtle.pendown()
turtle.goto(x2,y2)
turtle.write(str(x2)+","+str(y2))

turtle.done()