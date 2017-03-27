
def sumDigit(n):
    if n>0:
        return (n%10)+sumDigit(n//10)
    else:
        return 0
    
input=eval(input("enter an integer for summing digits"))
print("the sum of digits of",input,"is",sumDigit(input))