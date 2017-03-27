lst=[]
n = input("Enter list of 10 numbers:")

n = n.split()
for i in range(0,len(n)):
    m=int(n[i])
    lst.append(m)

def bubbleSort(lst):
    for j in range(0,len(lst)):
        for i in range(0,len(lst)):
            if i+1 ==len(lst):
                break
            if lst[i]<=lst[i+1]:
                continue
            else:
                lst[i],lst[i+1]=lst[i+1],lst[i]
    print(lst)
    
bubbleSort(lst)
        