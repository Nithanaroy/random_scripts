def checkAll(s, str, res, v):
    new_str = str
    for c in s:
        temp = new_str.replace(c, "", 1)
        if len(new_str) is len(temp):
            return str
        new_str = temp
    res.append(v)
    return new_str


def check(s):
    l = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    res = []
    i = 0
    while i < len(l):
        num = l[i]
        temp = checkAll(num, s, res, i)
        if len(temp) is len(s):
            i += 1
        s = temp

    return ''.join(map(str, res))


def main():
    t = int(raw_input())
    for i in range(1, t + 1):
        print "Case #%d: %s" % (i, check(raw_input()))


if __name__ == '__main__':
    main()
