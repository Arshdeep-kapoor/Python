def drawCircle(x,y,radius):
    import turtle
    turtle.penup() 
    turtle.goto(x, y - radius)
    turtle.pendown() 
    turtle.circle(radius)

def drawRectangle(x,y,width,height):
    import turtle
    turtle.penup() 
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown() 
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)

def drawPoint(x,y):
    import turtle
    turtle.penup() 
    turtle.goto(x, y)
    turtle.pendown() 
    turtle.begin_fill() 
    turtle.circle(3)
    turtle.end_fill() 
 

def main():
    import math
    import random
    
    drawCircle(50,0,50)
    drawRectangle(-75, 0, 100, 100)
    
    count=0
    
    while count<10:
        
        x1 = random.randint(-200, 200)
        y1 = random.randint(-200, 200)
        
        if x1 < -25 and x1 > -125 and y1 > -50 and y1 < 50:
            drawPoint(x1,y1)
            count=count+1
        else:
            continue
    
    count = 0
    
    while count<10:
        
        x = random.randint(-100,100)
        y = random.randint(-100,100)
        
        d= math.sqrt((x - 50) ** 2 + (y) ** 2)
        
        if 50**2 > d**2:
            drawPoint(x, y)
            count=count+1
        else:
            continue

main()