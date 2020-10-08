import fractions
from fractions import Fraction as F

def Anchosr(a):
    a = a.split(', ')
    s = F(a.pop(0))
    w = F(a.pop(0))
    pA = F(a.pop(0))
    cA = []
    for i in range(pA.numerator + 1):
        cA.append(F(a.pop(0)))
    pB = F(a.pop(0))
    cB = []
    for i in range(pB.numerator + 1):
        cB.append(F(a.pop(0)))
    print(s,w,pA,cA,pB,cB)
    return(0)
Anchosr('1, -1/8, 2, 1, -5/2, 1, 1, 1, 3')
