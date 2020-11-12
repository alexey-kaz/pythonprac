class nestr(str):
	def __neg__(self):
		return nestr(''.join(reversed(self)))
	

s = nestr(input())
print(eval(s))
