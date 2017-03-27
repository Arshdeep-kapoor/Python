print("Enter number separated by one space",end=" ")
n = input("to find the mean and Standard deviation:")
n=[eval(x) for x in n.split()]

def mean(x):    
    return (sum(x)/len(x))

def deviation(x):
    z=0
    for i in range(len(x)):
        z+=((x[i]-mean(x))**2)
    return ((z/(len(x)-1))**0.5)

print("The mean is",format(mean(n),"<10.2f"),"\n","The standard deviation is",format(deviation(n),"<10.5f"))