import turtle

for l in range(4):
    for k in range(2):
        for j in range(4):
            x="black"
            y="white"
            turtle.color(x,x)
            turtle.begin_fill()
            for i in range(4):
                turtle.left(90)
                turtle.forward(10)
            turtle.end_fill()
            turtle.right(90)
            turtle.color(x, y)
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(10)
                turtle.right(90)
            turtle.end_fill()
            turtle.penup()
            turtle.forward(20)
            turtle.left(90)
            turtle.pendown()
        turtle.penup()
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.pendown()
#    turtle.done()
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
turtle.done()


