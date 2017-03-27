s = ""
input=eval(input("enter the decimal number"))
r=0

def chang(r):
    return (chr(ord("A")+r-10))    

while input>0:
    r=input%16
    input=input//16
    if r>9:
        print(r)
        r=chang(r)
        print(r)
    else:
        r=str(r)
    s=r+s
    
print(s)    