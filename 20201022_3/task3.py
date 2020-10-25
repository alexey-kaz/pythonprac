from itertools import *

print(*filterfalse(lambda x: x.count('TOR') != 2, [''.join(i) for i in product('ORT', repeat=int(input()))]), sep='\n')
