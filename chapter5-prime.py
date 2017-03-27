count=0
number=2

print("the first 50 prime numbers are")

while count<50:
    
    isPrime=True
    
    divisor=2
    while divisor<=number/2:
        if number%divisor==0:
            isPrime=False
            break
        divisor+=1
    
    if isPrime:
        count+=1
        
        print(format(number,"5d"),end=" ")
        if count%10==0:
            print()
            
    number+=1