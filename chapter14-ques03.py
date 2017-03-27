ifile=input("Enter the file name to count the words in it")
ifh=open(ifile,"r")

dict={}
words=[]  

for i in ifh:
    words=i.strip()
    words=words.split()
    print(words)
    for j in words:
        dict[j] = dict.get(j, 0) + 1
    
for k,v in dict.items():
    print (k,v)