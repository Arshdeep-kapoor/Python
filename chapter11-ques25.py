matrix=[]
print("Enter a 3-by-3 matrix row by row:")

for row in range(3):
    matrix.append([])
    value=input("")
    value=value.split()
    for column in range(len(value)):
        matrix[row].append(value[column])    
    if row==2:
        break

def isMarkovMatrix(m):
    for column in range(3):
        s=0
        for row in range(3):
            if float(matrix[row][column])>0:
                s+=float(matrix[row][column])
            else:
                return False
        if s ==1:
            continue
        else:
            return False
    if s ==1:
        return True
    else:
        return False
    
if isMarkovMatrix(matrix):
    print("It is a Markov matrix")
else:
    print("It is not a Markov matrix")
    