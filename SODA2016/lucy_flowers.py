import math


def ncr(n, r):
    return math.factorial(n) / (math.factorial(n - r) * math.factorial(r))


def catlan(n):
    return math.factorial(2 * n) / (math.factorial(n + 1) * math.factorial(n))


mem_catlan = {}
mem_ncr = {}
mem_comb = {}
mod = int(math.pow(10, 9)) + 9


def find_comb(n):
    res = 0
    for i in range(1, n + 1):

        if (n, i) in mem_comb:
            res += mem_comb[(n, i)]
        else:
            ires = 0
            if i in mem_catlan:
                b = mem_catlan[i]
            else:
                b = catlan(i)
                mem_catlan[i] = b

            if (n, i) in mem_ncr:
                a = mem_ncr[(n, i)]
            else:
                a = ncr(n, i)
                mem_ncr[(n, i)] = a

            ires = a * b
            mem_comb[(n, i)] = ires
            res += ires
    if res > mod:
        return res % mod
    return res


def main():
    n = int(raw_input())
    for i in range(0, n):
        print find_comb(int(raw_input()))


if __name__ == '__main__':
    main()
