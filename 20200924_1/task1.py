n = int(input())
print([i for i in range(1,n) if all(i%d for d in range(2,i))])
