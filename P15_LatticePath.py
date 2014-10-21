__author__ = 'leon'


def lattic_path(num):
    num += 1
    dp = [[0 for j in range(num)] for i in range(num)]
    dp[0][0] = 1

    for i in xrange(1, num):
        dp[i][0] = 1

    for j in xrange(1, num):
        dp[0][j] = 1

    for i in xrange(1, num):
        for j in xrange(1, num):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    print dp[-1][-1]


lattic_path(20)