__author__ = 'leon'

def sumdiff(num):
    sumofsquare = 0
    squareofsum = 0
    for i in xrange(1, num + 1):
        sumofsquare += pow(i, 2)
        squareofsum += i

    squareofsum = pow(squareofsum, 2)
    return squareofsum - sumofsquare

print sumdiff(100)