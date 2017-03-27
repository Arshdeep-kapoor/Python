# Program to - Game: scissor, rock, paper

# program to play the game scissor, rock , paper

import random
i=j=0
for k in range(0,20):
    
    Comp = random.randint(0,2)
    User=eval(input(" Enter the Number [scissor (0), rock (1), paper (2)]:"))

    if Comp ==0:
        CompName = "Scissor"
    elif Comp == 1:
        CompName = "Rock"
    elif Comp == 2:
        CompName = "Paper"

    if User ==0:
        UserName = "Scissor"
    elif User == 1:
        UserName = "Rock"
    elif User == 2:
        UserName = "Paper"

        print ("Test:",Comp,CompName,User,UserName)

    if (Comp == 0 and User == 1):
        print ("Computer is",CompName,"You are",UserName,"You Won !!!")
        i += 1
    elif (Comp == 0 and User == 2):
        print ("Computer is",CompName,"You are",UserName,"You Lost !!!")
        j += 1
    elif (Comp == 1 and User ==0):
        print ("Computer is",CompName,"You are",UserName,"You Lost !!!")
        j += 1
    elif (Comp == 1 and User ==2):
        print ("Computer is",CompName,"You are",UserName,"You Won !!!")
        i += 1
    elif (Comp == 2 and User ==0):
        print ("Computer is",CompName,"You are",UserName,"You Won !!!")
        i += 1
    elif (Comp == 2 and User ==1):
        print ("Computer is",CompName,"You are",UserName,"You Lost !!!")
        j += 1   
    elif (Comp == User):
        print("Computer is",CompName,"You are",UserName,"Its is a draw")
    
    if(i==2 or j==2):
        break

if (i==2):
    print("The Game ended because user won more than twice")
elif (j==2):
    print("The Game ended because Computer won more than twice")