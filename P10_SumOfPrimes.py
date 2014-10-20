__author__ = 'leon'

TWO_MILLION = 2000000

numlist = [True for i in range(TWO_MILLION + 1)]
numlist[0] = False
numlist[1] = False

def prime_filter(numlist):
    index = 2
    size = len(numlist)
    while index < size:
        if numlist[index]:
            i = index * 2
            while i < size:
                numlist[i] = False
                i += index
        index += 1
        while index < size:
            if numlist[index]:
                break
            else:
                index += 1

prime_filter(numlist)

sum = 0
size = len(numlist)
for i in xrange(size):
    if numlist[i]:
        sum += i

print sum