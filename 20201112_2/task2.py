from collections import UserString


class nestr(UserString):
    def __neg__(self):
        return type(self)(''.join((str(i) for i in reversed(self))))


while s := input():
    print(eval(s))
