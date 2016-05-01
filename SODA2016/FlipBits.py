def getIntegerComplement(n):
    a = ''
    while n > 0:
        a = str((n % 2)) + a
        n /= 2
    b = '%032d' % int(a)
    c = ''
    for i in b:
        if i == '1':
            c += '0'
        else:
            c += '1'
    i = 1
    num = 0
    for j in xrange(len(c) - 1, -1, -1):
        num += i * int(c[j])
        i *= 2
    return num


def main():
    n = int(raw_input())
    while n > 0:
        inp = int(raw_input())
        if inp == 0:
            print 4294967295
        else:
            print getIntegerComplement(inp)
        n -= 1


if __name__ == '__main__':
    main()
