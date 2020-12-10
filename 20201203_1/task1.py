from types import FunctionType
from functools import wraps
import sys


def dumper(fun, name):
    @wraps(fun)
    def new_fun(*args, **kwargs):
        print("{0}: {1}, {2}".format(name, args[1:], kwargs))
        return fun(*args, **kwargs)

    return new_fun


class dump(type):
    def __init__(cls, *ap, **an):
        for i, j in vars(cls).items():
            if isinstance(j, FunctionType):
                setattr(cls, i, dumper(j, i))
        super().__init__(*ap, **an)


exec(sys.stdin.read())