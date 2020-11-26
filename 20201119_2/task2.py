import sys


class Num:
    num = 0

    def __init__(self):
        self.num = 0

    def __get__(self, obj, owner):
        if "num" in obj.__dict__:
            return obj.__dict__["num"]
        else:
            return self.__dict__["num"]

    def __set__(self, obj, val):
        if hasattr(val, "real"):
            obj.__dict__["num"] = val
        elif hasattr(val, "__len__"):
            obj.__dict__["num"] = len(val)


exec(sys.stdin.read())
