def solveSquare(a,b,c):
    d = b**2 - 4*a*c
    if d >= 0:
        return tuple(sorted((-b-d**(0.5)/(2*a),-b+d**(0.5)/(2*a))))
    else:
        return None
