def dominant(a, b):
    return a[0]<=b[0] and a[1]<=b[1] and (a[0]<b[0] or a[1]<b[1])

def Paretto(*x):
    return tuple([a for a in n if all([not dominant(a,b) for b in n])])

n = eval(input())
print(*Paretto(n))
