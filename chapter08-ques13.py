def prefix(str1,str2):
    str3=""
    if len(str1)>len(str2):
        m=len(str2)
    else:
        m=len(str1)
    for i in range(0,m):
        if str1[i]==str2[i]:
            str3+=str1[i]
    return str3

def main():
    str1=input("enter the string one:")
    str2=input("enter the string two:")
    
    str3=prefix(str1,str2)
    
    print("the longest common prefix of",str1,"and",str2,"is",str3)

main()
    