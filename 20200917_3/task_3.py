i=j=3
while i<=6:
    line=list()
    while j<=6:
        num = i*j
        dig = 0
        while num>0:
            dig += num%10
            num=int(num/10)
        if dig==6:
            line.append(':=)')
        else:
            line.append(i*j)
        j+=1
    print(*line, sep=' ')
    i+=1
    j=3
            
