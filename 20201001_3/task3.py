# Функционал-еval()-ище. Написать функцию calc(s, t ,u), которой передаются три строки. Каждая строка — это формула;
# s и t — над одной переменной x, а u — над двумя переменными x и y.
# Возвращается функция, которая по заданному x вычисляет u(s(x), t(x)).


def Calc(s, t, u):
    return lambda x: eval(u, {'x': eval(s), 'y': eval(t)})