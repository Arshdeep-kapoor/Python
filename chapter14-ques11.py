ifile=input("Enter the file name to count the words in it")
ifh=open(ifile,"r")

dictV={}
dictC={}
Vow={'a','e','i','o','u'}
words=[]  
letters=[]
for i in ifh:
    words=i.strip()
    words=words.split()
    for j in words:
        letters=list(j)
        for k in letters:
            if k.lower() in Vow:
                dictV[k.lower()] = dictV.get(k.lower(), 0) + 1
            else:
                dictC[k] = dictC.get(k, 0) + 1
    
print("All the vowels in the file is",dictV)

print("All the consonants are",dictC)