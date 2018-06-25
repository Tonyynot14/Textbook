# Creator:Tony Wade

# Reuse prime function
def prime(num):
    divisibleNums = 1
    for i in range(2, num):
        if num % i == 0:
            divisibleNums += 1

    if divisibleNums > 1 or num <= 1:
        return False
    else:
        return True

# Twin primes are prime numbers that are two numbers apart

def twinPrime(num):
    for i in range(2,num+1):
        if prime(i) and prime(i+2):
            print("(",i,",",i+2,")")

twinPrime(1000)