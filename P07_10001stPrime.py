__author__ = 'leon'

import math

def isPrime(num):
    if num%2 == 0:
        return False

    root = int(math.sqrt(num))
    for i in xrange(3, root+1):
        if num%i == 0:
            return False

    return True

def getNthPrime(n):
    count = 1
    number = 2
    while count  < n:
        number += 1
        if isPrime(number):
            count += 1

    return number


print getNthPrime(10001)

