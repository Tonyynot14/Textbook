def isPrime(number):
    newNum=int(number/2)
    for i in range(2,newNum):
        if number%i==0:
            return False
    return True



def numOfPrime(maxNumber):
    primes = 0
    for i in range(2,maxNumber):
        if isPrime(i):
            print(i,end=" ")
            primes+=1
        if primes%10==0 and isPrime(i-1):
            print()


numOfPrime(1000)