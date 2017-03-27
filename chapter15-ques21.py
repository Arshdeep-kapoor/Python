def binaryToDec (str, pow, total):
    if (len(str) == 1):
        return int(str) * (2 ** pow) + total
    else:
        num = int(str[-1:])
        total += (num * (2 ** pow))
        return binaryToDec(str[:-1], pow + 1, total)
print(binaryToDec(input("enter the number in binary"), 0, 0))