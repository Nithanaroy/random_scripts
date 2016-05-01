def fill(s1, s2):
    l = len(s1)
    s1 = list(s1)
    s2 = list(s2)
    for i in range(l - 1, -1, -1):
        c1 = s1[i]
        c2 = s2[i]
        if c1 is not '?' and c2 is not '?':
            pass
        elif c1 is '?' and c2 is '?':
            if i - 1 < 0:
                # this is the first character
                s1[i] = 0
                s2[i] = 0
            else:
                pc1 = s1[i - 1]
                pc2 = s2[i - 1]
                if pc1 is not '?' and pc2 is not '?':
                    if pc1 is pc2:
                        s1[i] = 0
                        s2[i] = 0
                    else:
                        if int(pc1) < int(pc2):
                            s1[i] = 9
                            s2[i] = 0
                        else:
                            s2[i] = 9
                            s1[i] = 0
                else:
                    s1[i] = 0
                    s2[i] = 0
        else:
            # only one of them is unknown
            if c1 is '?':
                s1[i] = s2[i]
            else:
                s2[i] = s1[i]

    # return ' '.join([''.join(map(str, s1)), ''.join(map(str, s2))])
    return ','.join([''.join(map(str, s1)), ''.join(map(str, s2))])


def main():
    t = int(raw_input())
    for i in range(1, t + 1):
        s1, s2 = raw_input().split(" ")
        # print "Case #%d: %s" % (i, fill(s1, s2))
        print "%s" % (fill(s1, s2))


if __name__ == '__main__':
    main()
