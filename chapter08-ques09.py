inputInBinary=input("enter the binary input to convert to hexa")

def check(l):
    return chr(ord('A')+(l-10))

def binaryToHex(binaryValue):
    hexOutput=""
    m = len(binaryValue)
    for i in range(1,m+1,4):
        l=0
        n=binaryValue[-i-3:-i]+binaryValue[-i]
        for m in range(0,len(n)):
            l+=(int(n[-m-1])*pow(2,m))
        if l>9:
            l=check(l)
        else:
            l=str(l)
        hexOutput=l+hexOutput
    return hexOutput

print(binaryToHex(inputInBinary))