day = eval(input("enter an integer for today day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6)"))
afterDay=eval(input("Enter the number of days elapsed since today:"))
altr=day
day+=afterDay
day%=7
if (day==1):
    day="Monday"
elif (day==2):
    day="Tuesday"
elif (day==3):
    day="Wednesday"
elif (day==4):
    day="Thursday"
elif (day==5):
    day="Friday"
elif (day==6):
    day="Saturday"
elif (day==0):
    day="Sunday"

if (altr==1):
    altr="Monday"
elif (altr==2):
    altr="Tuesday"
elif (altr==3):
    altr="Wednesday"
elif (altr==4):
    altr="Thursday"
elif (altr==5):
    altr="Friday"
elif (altr==6):
    altr="Saturday"
elif (altr==0):
    altr="Sunday"
    
print("Today is",altr,"and the future day is ",day)
    
    