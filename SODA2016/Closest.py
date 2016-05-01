import math


def closest(a, b, x):
    c = math.pow(a, b)
    d = int(c / x)
    m = d * x
    return m


def main():
    n = int(raw_input())
    while n > 0:
        a, b, x = [int(i) for i in raw_input().strip().split(" ")]
        print closest(a, b, x)
        n -= 1


if __name__ == '__main__':
    main()
