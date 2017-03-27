class Location(object):
    def __init__(self,row,column,maxValue):
        self.row = row
        self.column = column
        self.maxValue = maxValue

def locateLargest(a):
    max = a[0][0]
    row = 0
    col = 0
    for i in range (len(a)):
        for j in range (len(a[i])):
            if (a[i][j]>max):
                max=a[i][j]
                row=i
                col=j
    return Location(row,col,max)

def main():
    row,col = eval(input("Enter the number of rows and column in the list:"))
    matrix = []
    for i in range (row):
        matrix.append([float(x) for x in input("Enter row %d"%i).split()])
    maxLoc = locateLargest(matrix)
    print("The location of largest element",maxLoc.maxValue,"is at",\
          maxLoc.row,",",maxLoc.column)
        
main()