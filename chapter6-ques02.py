n = eval(input("please enter the number for digit add"))
#while lagao ...you dont need to ask for digits of number
def sumDigit(x):
    l = 0 
    y = 0
    while x != 0:
        l = x%10
        y += l
        x = x//10
    return y
   
s = sumDigit(n)
print("the sum of digits of",n,"is",s)