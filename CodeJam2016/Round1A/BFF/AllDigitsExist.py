"""
Given a number find by which multiple of that number, we can find all digits 0-9
N = 1692. found the digits 1, 2, 6, and 9.
2N = 3384. found the digits 1, 2, 3, 4, 6, 8, and 9.
3N = 5076. found all ten digits!
"""


def main(n):
    if n is 0:
        return 'INSOMNIA'
    d = [0] * 10
    if str(n).rstrip('0')[-1] != '5':  # if number doesn't end with 5 after removing trailing 0s
        if n % 2 == 0:
            return run(d, 46, n)  # 45 is when 2 finds all digits
        else:
            return run(d, 11, n)  # by 10 all odd numbers - { 5n } find all digits
    else:
        ans = run(d, 19, n)
        if ans == 'INSOMNIA' and d[9] == 0:
            s = 90
            while s % n is not 0:
                s *= 10
            return s
        return ans


def run(d, l, n):
    for i in range(1, l):
        m = n * i
        if track_digits(m, d) is 10:
            return m
    return 'INSOMNIA'


def track_digits(n, o):
    for d in str(n):
        o[int(d)] = 1
    return sum(o)


if __name__ == '__main__':
    t = int(raw_input())  # number of test cases
    for index in range(0, t):
        num = int(raw_input())
        print 'Case #%d: %s' % (index + 1, main(num))
