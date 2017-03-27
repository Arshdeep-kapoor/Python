passInput=input("Enter the password")
s=0
if len(passInput)>=8:
    if passInput.isalnum():
        for i in range(0,len(passInput)):
            if passInput[i].isdigit():
                s+=1
        if s >=2:
            print("valid password")
else:
    print("invalid password")