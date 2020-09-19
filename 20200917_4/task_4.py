a, n = eval(input())
x = y = z = 0
while x ** n + y ** n + z ** n < a:
    x += 1
    y = 0
    while x ** n + y ** n + z ** n < a:
        y = 1
        z = 0
        while x ** n + y ** n + z ** n < a:
            z += 1
            if x ** n + y ** n + z ** n > a:
                z -= 1
                break
        if x ** n + y ** n + z ** n > a:
            y -= 1
            break
    if x ** n + y ** n + z ** n > a:
        print('FAIL')
        break
else:
    print(x, y, z)
