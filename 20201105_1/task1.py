from re import *


def match_check(st):
    return bool(match(r"[+-]?(\d+|\d*\.\d+|\d+\.\d*)([eE][+-]?\d+)?$", st))


print(match_check(input()))
