#!usr/bin/env python3
a,b = input().split()

# qwe sdfgsdfg
# ->
#      qwe
# sdfgsdfg

L = max(len(a), len(b))
fmt = "{"+f"{L}"+"}"
print(fmt)
#print(fmt.format(a))
#print(fmt.format(b))
