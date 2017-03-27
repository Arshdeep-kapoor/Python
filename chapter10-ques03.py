print("Enter integers between 1 and 100",end=" ")
n = input("separated by one space:")

istring=n.split()
count=len(istring)*[0]
 
for i in range(len(istring)):
    m=istring[i]
    for j in range(len(istring)):
        if m == istring[j]:
            count[i]+=1
            if count[i]>1:
                istring.pop(j)
        if j+1==len(istring):
            break
    if i+1==len(istring):
        break

for i in range(len(istring)):
    print(istring[i],"occurs",count[i],"times")
    if i==len(istring)-1:
        break
    

