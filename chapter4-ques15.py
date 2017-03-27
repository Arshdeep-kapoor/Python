# Program to generate a three-digit lottery number and match the condition.
import random
lottery=random.randint(0,999)
x1=lottery//100
y1=lottery%100
y1=y1//10
z1=y1%10

guess = eval(input("Enter the three digits guess for the lottery"))

x2=guess//100
y2=guess%100
y2=y2//10
z2=y2%10

if (x1==x2 and y1==y2 and z1==z2):
    print("Since user input matches the lottery number in the exact order, the award is $10,000")

elif ((x1==x2 or x1==y2 or x1==z2) and (y1==x2 or y1==y2 or y1 ==z2) and (z1==x2 or z1==y2 or z1==z2)):
    print("Since all the digits in the user input match all the digits in the lottery number, the award is $3,000")

elif ((x1==x2 or x1==y2 or x1==z2) or (y1==x2 or y1==x2 or y1 ==z2) or (z1==x2 or z1==y2 or z1==z2)):
    print("Since one digit in the user input matches a digit in the lottery number, the award is $1,000")

else:
    print("SORRY, EVEN A SINGLE NUMBER DID NOT MATCH")
    
print ("The randomly generated lottery number is",lottery)
