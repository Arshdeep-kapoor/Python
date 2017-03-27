matrix=[]

rows=eval(input("enter the number of rows"))

for row in range(rows):
    print("Enter a",rows,"-by-",rows," matrix row for row ",row+1,end="")
    vale=input(": ")
    matrix.append(vale.split(" "))

s=0 

for row in range(rows):
    s+=float(matrix[row][row])

print("Sum of the elements in the major diagonal is",s)