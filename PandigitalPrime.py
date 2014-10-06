__author__ = 'leon'
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
'''

def permutation(numlist):
    if len(numlist) == 0:
        return []
    if len(numlist) == 1:
        return [numlist]
    res = []
    for i in xrange(len(numlist)):
        for j in permutation(numlist[0:i] + numlist[i + 1:]):
            res.append(j + [numlist[i]])
    return res


def isPrime(n):
    root = int(n ** 0.5)
    for k in xrange(2, root):
        if n % k == 0:
            return False
    return True


def getlargestpandigitalprime(numlist):
    for i in xrange(len(numlist), -1, -1):
        permut = permutation(numlist[:i])
        numbers = []
        for valuelist in permut:
            value = 0
            for i in xrange(len(valuelist)):
                value += valuelist[i] * pow(10, i)
            numbers.append(value)

        numbers.sort(reverse=True)

        for n in numbers:
            if isPrime(n):
                return n


numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print getlargestpandigitalprime(numlist)