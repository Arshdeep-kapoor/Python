n = eval(input("please enter the number for digit to check if it is palindrome"))
def reverse(x):
    l = 0 
    y = 0
    while x != 0:
        l = x%10
        y =(y*10)+ l
        x = x//10
    return y
def isPalindrome(number):
    if s == n:
        return True
    else:
        return False
       
s = reverse(n)
if isPalindrome(s):
    print(n,"is palindrome")
else:
    print(n,"is not palindrome")