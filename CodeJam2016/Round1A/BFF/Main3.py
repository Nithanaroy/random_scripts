"""
Problem

You are a teacher at the brand new Little Coders kindergarten. You have N kids in your class, and each one has a different student ID number from 1 through N. Every kid in your class has a single best friend forever (BFF), and you know who that BFF is for each kid. BFFs are not necessarily reciprocal -- that is, B being A's BFF does not imply that A is B's BFF.

Your lesson plan for tomorrow includes an activity in which the participants must sit in a circle. You want to make the activity as successful as possible by building the largest possible circle of kids such that each kid in the circle is sitting directly next to their BFF, either to the left or to the right. Any kids not in the circle will watch the activity without participating.

What is the greatest number of kids that can be in the circle?
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of two lines. The first line of a test case contains a single integer N, the total number of kids in the class. The second line of a test case contains N integers F1, F2, ..., FN, where Fi is the student ID number of the BFF of the kid with student ID i.
Output

For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the maximum number of kids in the group that can be arranged in a circle such that each kid in the circle is sitting next to his or her BFF.
Limits

1 <= T <= 100.
1 <= Fi <= N, for all i.
Fi != i, for all i. (No kid is their own BFF.)
Small dataset

3 <= N <= 10.
Large dataset

3 <= N <= 1000.
Sample

Input

Output


4
4
2 3 4 1
4
3 3 4 1
4
3 3 4 3
10
7 8 10 10 9 2 9 6 3 3



Case #1: 4
Case #2: 3
Case #3: 3
Case #4: 6

In sample case #4, the largest possible circle seats the following kids in the following order: 7 9 3 10 4 1.
(Any reflection or rotation of this circle would also work.) Note that the kid with student ID 1 is next to the
kid with student ID 7, as required, because the list represents a circle.
"""

# Note: My answer is incorrect

def dfs_start(g, s):
    v = []
    while s not in v:
        v.append(s)
        if s in g:
            s = g[s]
        else:
            break
    return v


def dfs_end(g, e):
    max_length = 0
    max_path = []
    for k in g.keys():
        p = dfs_start(g, k)
        if len(p) > max_length and p[-1] == e:
            max_length = len(p)
            max_path = p
    return max_path


def find_all(l, k):
    return [i + 1 for i, x in enumerate(l) if x == k]


def remove(h, v):
    for k in h.keys():
        if h[k] == v:
            h.pop(k)


def main(n, l):
    f = {}

    fs = map(int, l.split(" "))
    for i, af in enumerate(fs):
        f[i + 1] = af
    # print f

    max_depth = 0
    longest_path = []
    for i in range(0, n):
        path = dfs_start(f, i + 1)
        # print path
        if len(path) > max_depth:
            max_depth = len(path)
            longest_path = path
    # print longest_path

    while True:
        for p in longest_path:
            if p in f:
                f.pop(p)
            remove(f, p)

        a = set(longest_path)
        s2 = set(find_all(fs, longest_path[-1]))
        diff = s2 - a
        # print diff

        if len(diff) == 0:
            break

        max_depth = 0
        next_longest_path = []
        for n in diff:
            path = dfs_end(f, n)
            if len(path) > max_depth:
                max_depth = len(path)
                next_longest_path = path

        if len(next_longest_path) == 0:
            # This is the last node, just add any randomly to the path
            longest_path.append(diff.pop())

        longest_path.extend(reversed(next_longest_path))
        # print longest_path
    return len(longest_path)


if __name__ == '__main__':
    t = int(raw_input())
    i = 0
    while t > 0:
        print "Case #%d: %d" % (i + 1, main(int(raw_input()), raw_input()))
        t -= 1
        i += 1
