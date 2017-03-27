import turtle

x,y,l,w=eval(input("please enter center , length and width of rectangle"))
turtle.penup()
turtle.goto(x,y+w/2)
turtle.pendown()
turtle.forward(l/2)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(l)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(l/2)

turtle.done()