a = list(input().lower())
count = 0
found = list()
for i in range(len(a)-1):
    if a[i].isalpha():
        if a[i+1].isalpha() and ((a[i]+a[i+1]) not in found):
            count+=1
            print(a[i],a[i+1])
            found.append(a[i]+a[i+1])
print(count)
