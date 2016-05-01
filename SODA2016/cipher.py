def need_xor(a, given):
    if a == given:
        return 0
    return 1


def xor(s, k):
    x = need_xor(s[0], s[1])
    for i in s[2:k + 1]:
        x = need_xor(x, i)
    return x


def decipher(b, n, k):
    l = n + k - 1
    s = b[l - 1]
    x = int(s)
    for i in range(l - 2, l - k - 1, -1):
        z = need_xor(int(b[i]), x)
        x = need_xor(z, x)
        s = str(z) + s

    s1 = b[0]
    x = int(s1)
    for i in range(1, k - 1):
        z = need_xor(int(b[i]), x)
        x = need_xor(z, x)
        s1 += str(z)

    z = s1 + s
    if len(z) == n:
        return z

    for i in range(k - 1, n - len(z) + k - 1):
        s1 += str(xor(b[i - k + 1:i + 1], k))

    return s1 + s


def test_main():
    print decipher('1110001', 6, 2)


def main():
    n, k = [int(i) for i in raw_input().strip().split(" ")]
    b = raw_input().strip()

    print decipher(b, n, k)


if __name__ == '__main__':
    # test_main()
    main()