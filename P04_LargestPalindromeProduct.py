__author__ = 'leon'
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(num):
    k = 1
    while num // k >= 10:
        k *= 10

    while num > 0:
        lowest = num % 10
        highest = num // k
        if lowest != highest:
            return False
        num = (num - num // k * k) // 10
        k /= 100

    return True


def checker():
    maxproduct = 0
    for i in xrange(999, 99, -1):
        for j in xrange(999, 99, -1):
            product = i * j
            if isPalindrome(product):
                maxproduct = max(product, maxproduct)

    return maxproduct

print checker()