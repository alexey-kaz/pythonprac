# при помощи "регулярных" выражений, поменяйте в этой строке местами первое и второе вхождение последовательности
#   из от двух до четырех ненулевых цифр, слева и справа ограниченной нулями.
# Если вхождений меньше двух, не изменять строку

from re import sub

while s := input():
    print(sub(r"((?<=0)(?P<before>[1-9]{2,4})(?=0))(?P<zero>0*)((?<=0)(?P<after>[1-9]{2,4})(?=0))",
              r"\g<after>\g<zero>\g<before>", s))
