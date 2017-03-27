input=input("enter a string to count number of letters")

def countLetters(s):
    c=0
    for i in range(0,len(input)):
        if input[i].isalpha():
            c+=1
    return c

print(countLetters(input), "is total number of letters in the",input)