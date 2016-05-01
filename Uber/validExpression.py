def main(expr):
    openingParams = '({['
    closingParams = ')}]'
    stack = []
    for c in expr:
        if c in openingParams:
            stack.append(c)
        elif c in closingParams:
            topOfStack = stack.pop()
            openingIndex = openingParams.find(topOfStack)
            closingIndex = closingParams.find(c)
            if openingIndex is not closingIndex:
                return False
    if len(stack) == 0:
        return True
    return False


if __name__ =='__main__':
    print main('{(abc})')
