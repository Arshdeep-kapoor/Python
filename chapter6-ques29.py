CreditCardNum = eval(input("Please enter your credit card number"))

def isValid(number):
    if (getSize(number)>=13)or(getSize(number)<=16):
        print(getSize(number))
        if prefixMatched(number,getPrefix(number,2)):
            sumOfDoubleEven=sumOfDoubleEvenPlace(number)
            print(sumOfDoubleEven)
            sumOfOdd=sumOfOddPlace(number)
            print(sumOfOdd)
            total=sumOfDoubleEven+sumOfOdd
            if total%10==0:
                print("valid credit Card")
            else:
                print("invalid credit card number")

def sumOfDoubleEvenPlace(num):
    number=int(num)
    tenth=0
    sum=0
    while number>9:
        tenth=number%100
        tenth=2*(tenth//10)
        tenth=getDigit(tenth)
        sum+=tenth
        number=number//100
    return sum

def getDigit(num):
    tenth=num
    if tenth>9:
        tenth=1+(tenth%10)
    return tenth

def sumOfOddPlace(num):
    sum=0
    number=int(num)
    while number>0:
        sum+=(number%10)
        number=number//100
    return sum

def prefixMatched(num,d):
    if (d=="37")or (d[0]=="4")or(d[0]=="5")or(d[0]=="6"):
        return True
    return False

def getSize(number):
    number=str(number)
    return len(number)

def getPrefix(num,k):
    Number=str(num)
    if len(Number)>=k:
        return Number[0:k]
    else:
        return Number

isValid(CreditCardNum)