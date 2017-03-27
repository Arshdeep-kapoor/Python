# import csv #import the function CSV which helps python in importing
# # the excel file in csv format
# 
# # this will create a precision with 2 decimal places
# 
# with open('auto-mpg.csv') as csvfile:
#     mpg = list(csv.DictReader(csvfile))
#     #`csv.Dictreader` has read in each row of our csv file as a dictionary. 
#     #`len` shows that our list is comprised of 234 dictionaries.
# #print (mpg[:3])
# print (len(mpg))
# print (mpg[0].values())
# 
# #sum(float(d['cty']) for d in mpg) / len(mpg)
# 
# cylinders = set(d['cyl'] for d in mpg)
# cylinders
# 
# CtyMpgByCyl = []
# 
# for c in cylinders: # iterate over all the cylinder levels
#     summpg = 0
#     cyltypecount = 0
#     for d in mpg: # iterate over all dictionaries
#         if d['cyl'] == c: # if the cylinder level type matches,
#             summpg += float(d['cty']) # add the cty mpg
#             cyltypecount += 1 # increment the count
#     CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')
# 
# CtyMpgByCyl.sort(key=lambda x: x[0])
# CtyMpgByCyl
# 
# import datetime
# my_date = datetime.date(2016, 12, 21)
# import time
# 
# 
# class Person:
#     department = 'School of Information' #a class variable
# 
#     def set_name(self, new_name): #a method
#         self.name = new_name
#     def set_location(self, new_location):
#         self.location = new_location
#         
# person = Person()
# person.set_name('Christopher Brooks')
# person.set_location('Ann Arbor, MI, USA')
# print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))
# 
# store1 = [10.00, 11.00, 12.34, 2.34]
# store2 = [9.00, 11.10, 12.34, 2.01]
# cheapest = map(min, store1, store2)
# cheapest
# 
# for item in cheapest:
#     print(item)
import turtle

turtle.circle(100)
turtle.write("6")
turtle.penup()
turtle.goto(0,-30)
turtle.write("9:15:00")
turtle.goto(-100,100)
turtle.write("9")
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.pensize(2)
turtle.forward(80)
turtle.penup()
turtle.forward(15)
turtle.write("3")
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.left(90)
turtle.pensize(1)
turtle.forward(100)
turtle.write("12")
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.pensize(3)
turtle.left(90)
turtle.forward(65)



turtle.done()