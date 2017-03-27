def merge(list1, list2):  
    list3 = []
    i,j=0,0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i=i+1
        else:
            list3.append(list2[j])
            j=j+1
    
    while i < len(list1):
        list3.append(list1[i])
        i=i+1
    
    while j < len(list2):
        list3.append(list2[j])
        j=j+1
        
    return list3

list1 = []
list2 = []

n = input("Enter list one:")

n = n.split()

for i in range(0,len(n)):
    m=int(n[i])
    list1.append(m)
    
n = input("Enter list two:")

n = n.split()

for i in range(0,len(n)):
    m=int(n[i])
    list2.append(m)
    
list3 = merge(list1, list2)
print(list3)