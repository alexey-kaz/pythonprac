import re

expr = r'(?P<a>\(\d+,\d+\)), *(?P<b>\(\d+,\d+\)), *(?P<c>\(\d+,\d+\))'
while True:
    s = input()
    if re.search(expr, s):
        a = eval(re.fullmatch(expr, s).group('a'))
        b = eval(re.fullmatch(expr, s).group('b'))
        c = eval(re.fullmatch(expr, s).group('c'))
        A = abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2.0
        if A:
            print('{:.2f}'.format(A))
            break
        else:
            print('Not a triangle')
    else:
        print('Invalid input')
