__author__ = 'leon'
import math


def pythagorean():
    for a in xrange(1, 501):
        for b in xrange(a, 501):
            square_c = pow(a, 2) + pow(b, 2)
            c = int(math.sqrt(square_c))
            if pow(c, 2) == square_c:
                abc = a + b + c
                if abc == 1000:
                    return a * b * c


print pythagorean()