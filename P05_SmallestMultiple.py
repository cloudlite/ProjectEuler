__author__ = 'leon'
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# def smallestmultiple():
#     target = 21
#     while True:
#         founded = True
#         for i in xrange(1, 11):
#             founded = founded and (target % i == 0)
#             if not founded:
#                 target += 1
#                 break
#
#         if founded:
#             return target

# find all prime number in range (1, 20), multiple them
value = [16, 9, 5, 7, 11, 13, 17, 19] # 16 = 2^4, 9 = 3^2
res = 1
for i in value:
    res *= i

print res