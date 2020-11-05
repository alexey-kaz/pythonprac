from re import *
def match_check(st):
    return bool(match(r"[+-]?\d*.?\d+[Ee]*[+-]*\d*[^\w]", st))

while s := input():
    print(match_check(s))
