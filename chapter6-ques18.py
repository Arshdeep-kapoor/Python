import random
def printMatrix(numberOfrows):
    Number = 0
    for i in range(numberOfrows):
        for j in range(numberOfrows):
            Number = random.randint(0,1)
            print(Number, end = " ")
        print()
n= eval(input("Enter the number of rows and columns needed for matrix"))
printMatrix(n)