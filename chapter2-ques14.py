x1,y1,x2,y2,x3,y3 = eval(input("enter the three points of the triangle:"))
side1 = ((x1 - x2) * 2 + (y1 - y2) * 2) ** 0.5

side2 = ((x2 - x3) * 2 + (y2 - y3) * 2) ** 0.5

side3 = ((x1 - x3) * 2 + (y1 - y3) * 2) ** 0.5
s = float(side1+side2+side3)/2
area = ( s * (s-side1) * (s-side2) * (s-side3))**0.5

print("The area of the triangle is",area)