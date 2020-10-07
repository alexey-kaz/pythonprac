# Реализовать рекурсивную функцию бинарного поиска (проверки наличия) элемента в упорядоченной по неубыванию
#   индексируемой хранимой последовательности.
#
# на вход подаётся искомый элемент и последовательность, гарантированно упорядоченная по неубыванию



def Bisect(elem, seq):
    if not seq:
        return False
    mid = seq[(len(seq)-1)//2]
    if elem == mid:
        return True
    elif elem < mid:
        return Bisect(elem, seq[0:(len(seq)-1)//2])
    else:
        return Bisect(elem, seq[(len(seq)-1)//2 + 1:])
