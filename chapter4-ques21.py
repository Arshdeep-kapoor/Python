import math
year = eval(input("Enter the year[Ex:- 2008]:"))
m = eval(input("Enter the month:[1-12]:"))

if m == 1or m==2:
    m += 12
    year = year - 1
   
q = eval(input("Enter the day of the month:[1-31]:"))
j = math.floor(year/100)
k = year % 100

h = ((q+math.floor(26*(m+1)/10)+k+math.floor(k/4)+math.floor(j/4)+5*j) % 7)//1

if h==0:
    print("Day of the week is Saturday")
elif h==1:
    print("Day of the week is Sunday")
elif h==2:
    print("Day of the week is Monday")
elif h==3:
    print("Day of the week is Tuesday")
elif h==4:
    print("Day of the week is Wednesday")
elif h==5:
    print("Day of the week is Thursday")
elif h==6:
    print("Day of the week is Friday")