num = 97
sum=0
#check if number is ODD
if num%2==1:
#start calculating the sum
    for i in range(1,num+1,2):
        sum+=(i/(i+2))
else:
    num = eval(input("enter a odd number"))
print(sum)