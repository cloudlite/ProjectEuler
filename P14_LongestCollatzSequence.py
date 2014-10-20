__author__ = 'leon'

def longest_sequence(num):
    max_len = 0
    dict = {1: 1}
    for i in xrange(2, num + 1):
        if not dict.has_key(i):
            tmp = [i]
            curr_len = 1
            while tmp[-1] != 1:
                if tmp[-1] % 2 != 0:
                    next = tmp[-1] * 3 + 1
                    if dict.has_key(next):
                        curr_len += dict[next]
                        break
                    else:
                        tmp.append(next)
                else:
                    next = tmp[-1] / 2
                    if dict.has_key(next):
                        curr_len += dict[next]
                        break
                    else:
                        tmp.append(next)

                curr_len = len(tmp)

            dict[i] = curr_len
            if curr_len > max_len:
                max_len = curr_len
                res = i

    print max_len, res

longest_sequence(1000000)

