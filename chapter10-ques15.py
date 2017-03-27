def isSorted(lst):
    for i in range(0, len(lst)):
        if i+1==len(lst):
            break
        if lst[i+1]>=lst[i]:
            continue
        else:
            return False
    return True

lst=[]
n = input("Enter list:")

n = n.split()

for i in range(0,len(n)):
    m=int(n[i])
    lst.append(m)

if isSorted(lst):
    print("The list is already sorted")
else:
    print("The list is not sorted")