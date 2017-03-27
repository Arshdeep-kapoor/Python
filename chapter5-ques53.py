# Program to Turtle: plot the sine and cosine functions

import math
import turtle
turtle.pendown()
turtle.goto(0,0)
turtle.pensize(3)
turtle.forward(650)
turtle.right(180)
turtle.forward(1300)
turtle.right(180)
turtle.forward(650)
turtle.right(90)
turtle.forward(200)
turtle.right(180)
turtle.forward(400)
turtle.right(180)
turtle.forward(200)
turtle.color("RED")
turtle.penup()
turtle.goto(-630,80)
turtle.pendown()
for angle in range(-630,630):
    y = math.sin(math.radians(angle))
    turtle.goto(angle,y*80)
turtle.penup()
turtle.goto(-630,0)
turtle.color("Blue")
turtle.pendown()
for angle in range(-630,630):
    y = math.cos(math.radians(angle))
    turtle.goto(angle,y*80)
turtle.penup()
turtle.goto(-180,0)
turtle.pendown()
turtle.color("Black")
turtle.write("-180")
turtle.penup()
turtle.goto(180,0)
turtle.pendown()
turtle.write("180")
turtle.penup()
turtle.goto(0,0)
turtle.right(180)
turtle.forward(200)
turtle.done()