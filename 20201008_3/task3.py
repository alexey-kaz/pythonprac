num, length = eval(input())
sec = minimal = 1
offset = len(str(num))
last_arg = len(str(num * num))
out = ''
form = '{:{}d} * {:<{}d}= {:<{}d}'
column_len = len(form.format(1, offset, 1, offset + 1, 1, last_arg))
out_str = ''
space_str = ''.ljust(length, '=')
while True:
    print(space_str)
    for j in range(1, num + 1):
        temp_len = length
        sec = minimal
        enf_flag = True
        while temp_len > column_len:
            out = form.format(sec, offset, j, offset + 1, j * sec, last_arg)
            temp_len -= column_len
            if temp_len - 3 > column_len and sec < num:
                out_str += out + ' | '
                temp_len -= 3
            else:
                out_str += out
                print(out_str)
                out_str = ''
                temp_len = 0
            sec += 1
            if sec > num:
                break
    minimal = sec
    if sec > num:
        break
print(space_str)
