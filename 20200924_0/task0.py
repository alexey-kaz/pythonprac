for i in range(3,7):
    for j in range(3,7):
        if i*j//10 + i*j%10 == 6:
            print(':=)', end = ' ')
        else:
            print(i*j, end = ' ')
    print()
