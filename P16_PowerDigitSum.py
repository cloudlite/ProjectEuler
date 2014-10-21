__author__ = 'leon'

power_num = pow(2, 1000)
sum = 0

while power_num > 0:
    sum += power_num % 10
    power_num /= 10

print sum