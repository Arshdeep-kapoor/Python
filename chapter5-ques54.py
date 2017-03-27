# Program to draw Turtle: plot the square function

import math
import turtle
turtle.pendown()
turtle.goto(0,0)
turtle.pensize(3)
turtle.forward(400)
turtle.right(180)
turtle.forward(800)
turtle.right(180)
turtle.forward(400)
turtle.right(90)
turtle.forward(250)
turtle.right(180)
turtle.forward(500)
turtle.right(180)
turtle.forward(250)
turtle.color("RED")
turtle.penup()
turtle.goto(-16,256)

turtle.pendown()
for x in range(-16,17):
    y = x * x
    turtle.goto(x,y)

turtle.done()