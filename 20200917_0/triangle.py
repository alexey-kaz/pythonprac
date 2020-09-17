a,b,c = eval(input())
if a>0 and b>0 and c>0 and a+b>c and b+c>a or a+c>b:
	print("triangle")
else:
	print("not triangle")
