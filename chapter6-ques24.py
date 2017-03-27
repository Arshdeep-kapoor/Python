def isPalindrome(x):
    n=0
    n=x
    l = 0 
    y = 0
    while x != 0:
        l = x%10
        y =(y*10)+ l
        x = x//10
    if n==y :
        return True
    else:
        return False
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False # number is not a prime
        divisor += 1     
    return True # number is prime

def printPrimeNumbers(numberOfPrimes=100):
#    NUMBER_OF_PRIMES = 50 # Number of primes to display
#   NUMBER_OF_PRIMES_PER_LINE = 10 # Display 10 per line
    count = 0 # Count the number of prime numbers
    number = 2 # A number to be tested for primeness

# Repeatedly find prime numbers
    while count < numberOfPrimes:
# Print the prime number and increase the count
        if isPrime(number):
            if isPalindrome(number)==True:
                count += 1 # Increase the count
                print(number, end = " ")
                if count % 10 == 0:          
# Print the number and advance to the new line
                    print()
# Check if the next number is prime
        number += 1

print("The first 50 prime numbers are")
printPrimeNumbers()