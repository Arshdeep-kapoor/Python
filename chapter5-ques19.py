n = eval(input("Enter the number of lines: 1:15: "))
      
for i in range(1,n+1):
            
    for j in range(n-i):
        
        print("   ", end = "")
                
    if i > 1:
        
        for k in range(i,1,-1):
            
            print(format( k,"3d"), end="")
    
    for l in range(1,i+1):
        
        print(format(l,"3d"),end="")
    
    print()