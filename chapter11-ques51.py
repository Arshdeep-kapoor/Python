inp=input("Enter students names and scores:")
inp=inp.split()

list1,list2=[],[]
x=len(inp)
for i in range(x//2):
    list1.append([])
    for j in range(2):
        list1[i].append(inp[j])
        if j+1==2:
            break
    inp.pop(j)
    inp.pop(j-1)
    if i+1==(x//2):
        break

for k in range(len(list1)):
    list2.append([])
    list2[k].append(list1[k][1])
    list2[k].append(list1[k][0])
    
list2.sort()

for i in range(len(list2)):
    list2[i].reverse()
    print(list2[i])