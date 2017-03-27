ifile=input("Enter a filename:")
ifh=open(ifile)

words=[]
total,lines,letters=0,0,0

for i in ifh:
    lines+=1
    words=i.strip()
    words=words.split()
    for j in words:
        total+=1
        for k in j:
            letters+=1

print(letters," characters")
print(total," words")
print(lines," lines")