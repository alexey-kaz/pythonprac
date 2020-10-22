def ifun():
    i = 1
    while i:
        yield i**2
        i+=1

I = ifun()

print(*I)
