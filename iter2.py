def fib(m,n):
    a = 1
    b = 1
    for i in range(n):
        if i+1 >= m:
            yield a
        a, b = b, a+b

print(*fib(3,5))
