import math
x1,y1,r1 = eval(input("Enter circle1's center x-, y-coordinates, and radius:"))
x2,y2,r2= eval(input("Enter circle2's center x-, y-coordinates, and radius:"))

d=math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))

if d < abs(r1-r2):
    print("circle2 is inside circle1")
elif (d<(r1+r2)and d!=0):
    print("circle2 overlaps circle1")
elif ((r1==r2)and(x1==x2)and(y1==y2)) :
    print("both circles are same")