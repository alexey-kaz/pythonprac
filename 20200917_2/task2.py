s = 0
a = int(input())
while a>0:
	s += a
	if s>21:
		print(s)
		break
	a = int(input())
else:
        print(a)
