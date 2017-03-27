n1,n2 =0,0
while (n1==0) or (n2==0):
    n1,n2 = eval(input("enter the two numbers to find GCD"))
d =0
if n1>n2:
    d=n2
else:
    d = n1
for i in range(d,0,-1):
    if n2%i==0:
        if n1%i==0:
            break
        else:
            continue
    continue
print(d,"is the GCD")