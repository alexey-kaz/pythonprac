# Ввести строки (конец ввода — пустая строка). Выввести (в порядке ввода) только те строки,
# все символы которых не встречаются в других введённых строках.

a = []
b = []
while n:=input():
    a.append(n)
    b+=set(n)
c = set(b)
for i in c:
    for j in b:
        if i == j:
            b.remove(j)
            break
for i in a:
    for j in b:
        if j in i:
            break
    else:
        print(i)