from sympy import *

def isPrime(number):
    return isprime(number)

def primes_in_range(start, end):
    primeArr = []

    for x in range(start, end+1):
        if isprime(x) == True:
            primeArr.append(x)
    
    return primeArr

print(isPrime(7)) # True
print(isPrime(10)) # False

print(primes_in_range(1, 10)) # [2, 3, 5, 7]
