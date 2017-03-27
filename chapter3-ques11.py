number=eval(input("enter the four-digit number to be reversed"))
a=number//1000
b=number%10
c=((number%100)-b)//10
d=(number%1000-number%100)//100
Rev=a+d*10+c*100+b*1000
print("The reversed number is",Rev)