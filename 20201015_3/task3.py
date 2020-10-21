import re
from random import *
from sys import *


pass_len = int(argv[1])
if len(argv) > 2:
    s = int(argv[2])
else:
    s = randrange(1000)
    print(f"Seed: {s}")
seed(s)
dictionary = {}
try:
    while string := input().lower():
        s = re.sub('r[^а-я a-z]', '', string).split(' ')
        for a in s:
            for i in range(len(a) - 1):
                if a[i].isalpha() and a[i + 1].isalpha():
                    dictionary[a[i] + a[i + 1]] = dictionary.get(a[i] + a[i + 1], 0) + 1
except EOFError:
    pass
letter = choices(list(dictionary.keys()), list(dictionary.values()))
password = str(letter[0][0])
for i in range(pass_len-1):
    temp_dict = {}
    for j in dictionary:
        if j[0] == password[i]:
            temp_dict[j] = dictionary[j]
    letter = choices(list(temp_dict.keys()), list(temp_dict.values()))
    password += letter[0][1]
print(password)
