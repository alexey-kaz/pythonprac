import sys
from random import random


def checker(cls):
    for i, j in cls.__annotations__.items():
        if not hasattr(cls, i) or not (isinstance(getattr(cls, i), j)):
            return False
    return True


class check(type):

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.check_annotations = checker


exec(sys.stdin.read())