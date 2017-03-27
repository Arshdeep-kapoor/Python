ifile=input("Enter a filename:")
ifh=open(ifile)

words=[]
total,count=0,0
for i in ifh:
    words=i.strip()
    words=words.split()
    for j in words:
        total+=float(j)
        count+=1

print("There are",count,"scores")
print("The total is",total)
print("The average is",format(total/count,"<10.2f"))