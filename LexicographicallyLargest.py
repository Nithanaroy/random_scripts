"""
Given a string and valid swaps, find the lexicographically largest (LL) string

s = 'abc'
valid swaps = [(1,2), (2,3)] # string index starting from 1
LL string for s = 'cba'
Path from 'abc' to 'cba' => bac, bca, cba
"""

"""
Note: Current solution may not work if string contains duplicate characters :(
"""


def upsert(h, k, v):
    if k in h:
        h[k].append(v)
    else:
        h[k] = [v]


def highest(a, k, c, i):
    try:
        for j in k[i]:
            if c < a[j]:
                return j
    except:
        pass  # Ignore unknown indices
    return i


def update(h, k, old, new):
    i = h[k].index(old)
    h[k][i] = new


def find(h, k):
    return h[k][0]


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def ll(s, sw):
    swap_pos = {}
    char_pos = {}
    s1 = sorted(list(s))
    s = list(s)
    for i, c in enumerate(s1):
        upsert(char_pos, c, i)
    for e in sw:
        upsert(swap_pos, e[0] - 1, e[1] - 1)  # convert 1 based indexing to 0 based
    for k in swap_pos:
        swap_pos[k].sort(reversed)

    while len(s1) > 0:
        e = s1.pop(0)
        i = find(char_pos, e)
        while True:
            j = highest(s, swap_pos, e, i)
            if j == i:
                break
            update(char_pos, s[i], i, j)
            update(char_pos, s[j], j, i)
            swap(s, i, j)
            i = j
    return ''.join(s)


def main():
    print ll('abbc', [(1, 2), (2, 3)])


if __name__ == '__main__':
    main()
