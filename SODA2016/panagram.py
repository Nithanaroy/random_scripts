def isPanagram(s):
    l = {}
    for c in s.strip().lower():
        if c not in l:
            l[c] = 1
    for k in 'abcdefghijklmnopqrstuvwxyz':
        if k not in l:
            return 'not pangram'
    return 'pangram'


def main():
    s = raw_input()
    print isPanagram(s)


if __name__ == '__main__':
    main()
