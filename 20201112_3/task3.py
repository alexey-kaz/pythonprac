import re

expr = r'(?P<x>\(-?\d+, *-?\d+\)), *(?P<y>\(-?\d+, *-?\d+\)), *(?P<z>\(-?\d+, *-?\d+\))'
while True:
    try:
        s = input()
        if re.search(expr, s):
            x = eval(re.fullmatch(expr, s).group('x'))
            y = eval(re.fullmatch(expr, s).group('y'))
            z = eval(re.fullmatch(expr, s).group('z'))
        else:
            print('Invalid input')
            continue
        a = ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
        b = ((x[0] - z[0]) ** 2 + (x[1] - z[1]) ** 2) ** 0.5
        c = ((z[0] - y[0]) ** 2 + (z[1] - y[1]) ** 2) ** 0.5
        p = (a + b + c) / 2
        A = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        if A:
            print('{:.2f}'.format(A))
            break
        else:
            print('Not a triangle')
            continue
    except EOFError:
        break

