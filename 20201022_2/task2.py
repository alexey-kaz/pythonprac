def even(seq):
    for i in seq:
        if not i%2:
            yield i

def slide(seq):
    for i in range(len(seq)-2):
        yield from even(seq[i : i+3])

a = slide([3, 4, 6, 8, 11])
print(*a)
