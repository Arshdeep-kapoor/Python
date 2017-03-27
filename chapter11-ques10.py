matrix,sum_of_row,sum_of_column=[],[],[]
import random

for row in range(4):
    matrix.append([])
    for column in range(4):
        matrix[row].append(random.randint(0,1))
    print(matrix[row])
    sum_of_row.append(sum(matrix[row]))
    
def maxFound(sum_of_row):
    max_of_row=[]
    for row in range(4):
        if max(sum_of_row)==sum_of_row[row]:
            max_of_row.append(row)
    return max_of_row
            
for column in range(4):
    s=0
    for row in range(4):
        s+=matrix[row][column]
    sum_of_column.append(s)
    
print("the largest row index",maxFound(sum_of_row))
print("the largest column index",maxFound(sum_of_column))