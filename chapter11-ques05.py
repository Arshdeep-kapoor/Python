matrix1,matrix2=[],[]
m1,m2=[],[]

print("Enter Matrix1",end="")
input1=input(":")

print("Enter Matrix2",end="")
input2=input(":")

def matrix(m):
    matrix1=[]
    j,k=0,0
    for j in range(3):
        matrix1.append([])
        for k in range(3):
            matrix1[j].append(m[0])
            m.remove(m[0])
            if k==2:
                break
        if j+1==3:
            break
    return matrix1

m1=input1.split(" ")
matrix1=matrix(m1)

m2=input2.split(" ")
matrix2=matrix(m2)

def addMatrix(a, b):
    matrix=[]
    i,j=0,0
    for i in range(3):
        matrix.append([])
        for j in range(3):
            matrix[i].append(float(a[i][j])+float(b[i][j]))
            if j==2:
                break
        if i==2:
            break
    return matrix
            
print("The matrices are added as follows:")
print(matrix1[0],"\t  ",matrix2[0],"\t ",addMatrix(matrix1,matrix2)[0])
print(matrix1[1],"   + ",matrix2[1],"   =",addMatrix(matrix1,matrix2)[1])
print(matrix1[2],"\t  ",matrix2[2],"\t ",addMatrix(matrix1,matrix2)[2])

