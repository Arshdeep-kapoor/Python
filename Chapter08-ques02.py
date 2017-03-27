strLong=input("enter the main string")
checkStr=input("enter the string that has to be checked")

def find(s,n):
    if n in s:
        return True
    
    return False

if find(strLong,checkStr):
    print(checkStr,"is in",strLong)
else:
    print(checkStr,"is not in",strLong)
