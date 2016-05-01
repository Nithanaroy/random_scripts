"""
Status: Current code has stack overflow problem for long strings
"""


def lenardo_substrings(s, start, end):
    found = False
    for i in range(start, end):
        substring = s[i:i + 2]
        if substring == '00' or substring == '11':
            left = lenardo_substrings(s, start, i)
            right = lenardo_substrings(s, i + 1, end)
            found = True
            break
    if not found:
        len = end - start + 1
        return len * (len + 1) / 2
    return left + right


def main():
    n = int(raw_input())
    while n > 0:
        s = raw_input()
        print lenardo_substrings(s, 0, len(s) - 1)
        n -= 1


if __name__ == '__main__':
    main()
