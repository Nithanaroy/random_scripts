"""
Given a squared sized grid GG of size NN in which each cell has a lowercase letter. Denote the character in the iith row and in the jjth column as G[i][j]G[i][j].

You can perform one operation as many times as you like: Swap two column adjacent characters in the same row G[i][j]G[i][j] and G[i][j+1]G[i][j+1] for all valid i,ji,j.

Is it possible to rearrange the grid such that the following condition is true?

G[i][1]≤G[i][2]≤⋯≤G[i][N]G[i][1]≤G[i][2]≤⋯≤G[i][N] for 1≤i≤N1≤i≤N and
G[1][j]≤G[2][j]≤⋯≤G[N][j]G[1][j]≤G[2][j]≤⋯≤G[N][j] for 1≤j≤N1≤j≤N
In other words, is it possible to rearrange the grid such that every row and every column is lexicographically sorted?

Note: c1≤c2c1≤c2, if letter c1c1 is equal to c2c2 or is before c2c2 in the alphabet.

Input Format

The first line begins with TT, the number of testcases. In each testcase you will be given NN. The following NN lines contain NN lowercase english alphabet each, describing the grid.

Output Format

Print TT lines. On the iith line print YES if it is possible to rearrange the grid in the iith testcase or NO otherwise.

Constraints
1≤T≤1001≤T≤100
1≤N≤1001≤N≤100
GijGij will be a lower case letter

Sample Input

1
5
ebacd
fghij
olmkn
trpqs
xywuv
Sample Output

YES
Explanation

The grid in the first and only testcase can be reordered to

abcde
fghij
klmno
pqrst
uvwxy
This fulfills the condition since the rows 1, 2, ..., 5 and the columns 1, 2, ..., 5 are all lexicographically sorted.
"""


def is_sorted(g):
    for i, l in enumerate(g):
        g[i] = ''.join(sorted(l))
    for i in range(0, len(g[0])):
        for j in range(0, len(g) - 1):
            if g[j][i] > g[j + 1][i]:
                return 'NO'
    return 'YES'


def main():
    t = int(raw_input())
    for j in range(0, t):
        n = int(raw_input())
        g = []
        for i in range(0, n):
            g.append(raw_input())
        print is_sorted(g)


if __name__ == '__main__':
    main()
