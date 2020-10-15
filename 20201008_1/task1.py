from math import *


def fun(f):
    s = input().split(',')
    a, b, c, d = int(s[0]), int(s[1]), int(s[2]), int(s[3])
    step_x = (b - a) / 79
    step_y = (d - c) / 24
    terminal = []
    for i in range(80):
        terminal.append([])
        for j in range(25):
            terminal[i].append(" ")
    for i in range(0, 80):
        y = float(f(a + i * step_x))
        delta = abs(y - d)
        k = 0
        for j in range(0, 25):
            if delta > abs(y - d + j * step_y):
                delta = abs(y - d + j * step_y)
                k = j
        terminal[i][k] = "●"
    for j in range(0, 25):
        line = ""
        for i in range(0, 80):
            line += terminal[i][j]
        print(line)


func = input()
fun(lambda x: eval(func))
