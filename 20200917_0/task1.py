d = int(input())
a,b,c='-','-','-'
if d%25==0:
	if d%2==0:
		a='+'
	else:
		b='+'
if d%8==0:
	c='+'
print('A'+a+'B'+b+'C'+c)
