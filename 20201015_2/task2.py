# Генерация произносимого пароля
#
# произносимый пароль состоит из "слогов" трёх видов: 'Г', 'ГС' 'СГ',
#       где 'Г' - заглавная гласная буква, 'С' - заглавная согласная буква (Ь и Ъ не используем)
#
# на вход подаётся длина пароля (целое положительное число N)
# требуется сгенерировать пароль длины N путём его достройки, начиная с пустой строки,
#       до требуемой длины путём добавления случайного слога одного из описанных выше видов
# к частично построенной строке длины (N-1) разрешается добавлять последний слог из двух букв


from random import *
from sys import argv

glas = list('АЕЁИОУЫЭЮЯ')
soglas_space = soglas = list('БВГДЖЗКЛМНПРСТФХЦЧШЩ')
soglas_space.append('')
all_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯ'
passw_len = int(argv[1])
passw = ''
len = 0
while len < passw_len:
    rand_letter1 = choice(all_letters)
    if rand_letter1 in glas:
        rand_letter2 = choice(soglas_space)
    else:
        rand_letter2 = choice(glas)
    passw += rand_letter1 + rand_letter2
    len += 1 + (rand_letter2 != '')
print(passw)