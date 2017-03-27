import math

x1,y1 = 33.3590320,-84.2226589        #Atlanta GA

x2,y2 = 28.5383355,-81.37923649999999 #Orlando,FL

x3,y3 = 32.0835407,-81.09983419999998 #Savannah GA

x4,y4 = 35.2270869,-80.84312669999997 #Charlotte NC

radius = 6371.01

x1 = math.radians(x1)
x2 = math.radians(x2)
x3 = math.radians(x3)
x4 = math.radians(x4)
y1 = math.radians(y1)
y2 = math.radians(y2)
y3 = math.radians(y3)
y4 = math.radians(y4)

d12 = radius * (math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2)))
d23 = radius * (math.acos(math.sin(x2) * math.sin(x3) + math.cos(x2) * math.cos(x3) * math.cos(y2 - y3)))
d13 = radius * (math.acos(math.sin(x1) * math.sin(x3) + math.cos(x1) * math.cos(x3) * math.cos(y1 - y3)))
d14 = radius * (math.acos(math.sin(x1) * math.sin(x4) + math.cos(x1) * math.cos(x4) * math.cos(y1 - y4)))
d34 = radius * (math.acos(math.sin(x3) * math.sin(x4) + math.cos(x3) * math.cos(x4) * math.cos(y3 - y4)))

s = (d12 + d23 + d13) / 2

area1 = (s * (s - d12) * (s - d23) * (s - d13)) ** 0.5

s = (d13 + d14 + d34) / 2

area2 = (s * (s - d13) * (s - d14) * (s - d34)) ** 0.5

tot_area = area1 + area2

print("Estimated area enclosed by given cities is ", format(tot_area, '.2f' ))