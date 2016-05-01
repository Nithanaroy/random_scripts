# Enter your code here. Read input from STDIN. Print output to STDOUT
N, l = map(int, raw_input().split())

m = []
for i in xrange(l):
    a, b = map(int, raw_input().split())
    found = False
    for s in m:
        if a in s or b in s:
            s.add(a)
            s.add(b)
            found = True
            break
    if not found:
        m.append(set([a, b]))

result = 0
for i in range(0, len(m)):
    for j in range(i + 1, len(m)):
        result += len(m[i]) * len(m[j])
print result
