matrix,largest_element=[],[]
import random

rows=eval(input("Enter the number of rows in the list:"))

for row in range(rows):
    matrix.append([])
    value=input("Enter a row:")
    value=value.split()
    for column in range(len(value)):
        matrix[row].append(value[column])
    if row==rows-1:
        break
    
largest=float(matrix[0][0])
k,l=0,0

for row in range(rows):
    for columns in range(4):
        if largest<float(matrix[row][columns]):
            largest=float(matrix[row][columns])
            k=row
            l=columns
        if columns+1==len(matrix[row]):
            break
    if row+1==rows:
        break
                     
largest_element.append(k)
largest_element.append(l)
           
print("the location of largest element is",largest_element)