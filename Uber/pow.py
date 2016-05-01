def pow(a, b):
    if b > 1:
        x = pow(a * a, b / 2)
    if a % 2 != 0:
        return x * a
    return x

if __name__ == '__main__':
    print pow(3, 7)
