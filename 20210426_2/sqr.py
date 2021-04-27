def solveSquare(a, b, c):
    if a == 0:
        if b != 0:
            return str(-c/b)
        else:
            if c == 0:
                return "∞"
            else:
                return "∅"
    d = b ** 2 - 4 * a * c
    if d >= 0:
        return ','.join(map(str, set(sorted(((-b - d ** 0.5) / (2 * a), (-b + d ** 0.5) / (2 * a))))))
    else:
        x = (b - d ** 0.5) / (2 * a)
        s1 = ' - ' if x.imag < 0 else ' + '
        s2 = ' + ' if x.imag < 0 else ' - '
        return "{}{}{}i, {}{}{}i".format(x.real, s1, abs(x.imag), x.real, s2, abs(x.imag))
