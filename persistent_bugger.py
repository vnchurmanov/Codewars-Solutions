def multiply(solid_number):
    x = None
    res = 1
    for i in str(solid_number):
        if not x:
            x = int(i)
            res = int(i)
        else:
            res *= int(i)
    return res


def persistence(n):
    steps = 0
    b = str(n)
    while len(b) != 1:
        y = multiply(b)
        steps += 1
        b = str(y)
    return steps
