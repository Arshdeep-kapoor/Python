# (Display the first days of each month)

# Program to Display the first days of each month
Year,Fday=eval(input("Enter the year and First day of the year [0-sunday...6-saturday]:"))
days = 0
for i in range(0,12):
    if (i==1 or i==3 or i==5 or i==7 or i==8 or i == 10 or i==12):
        days = 31
    elif (i==2):
        days = 28
    elif (i==4 or i== 6 or i==9 or i== 11):
        days = 30
    
    Fday = Fday + days
    day = Fday % 7
    
    if day == 0:
        dayN = "Sunday"
    elif day==1:
        dayN = "Monday"
    elif day==2:
        dayN = "Tuesday"
    elif day==3:
        dayN = "Wednesday"
    elif day==4:
        dayN ="Thursday"
    elif day==5:
        dayN="Friday"
    elif day==6:
        dayN="Saturday"

    if i==0:
        MonN="January"
    elif i==1:
        MonN="February"
    elif i==2:
        MonN="March"
    elif i==3:
        MonN="April"
    elif i==4:
        MonN="May"
    elif i==5:
        MonN="June"
    elif i==6:
        MonN="July"
    elif i==7:
        MonN="August"
    elif i==8:
        MonN="September"
    elif i==9:
        MonN="October"
    elif i==10:
        MonN="November"
    elif i==11:
        MonN="December"
    
    print (MonN,"1st",Year,"is",dayN)