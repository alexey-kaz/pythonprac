# Написать декоратор, который считает кол-во вызовов функции и выводит его
#   с использованием глобальной переменной
import sys


def counter(fun):
    count = 0

    def wrap(*args, **dict_args):
        nonlocal count
        count += 1
        res = fun(*args, **dict_args)
        print('Function call count:', count)
        return res

    count = 0
    return wrap


exec(sys.stdin.read())
