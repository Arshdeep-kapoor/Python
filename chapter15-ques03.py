input1=eval(input("enter the first number"))
input2=eval(input("enter the second number"))

def gcd(m,n):
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)
    
print("the GCD of",input1,"and",input2,"is",gcd(input1,input2))