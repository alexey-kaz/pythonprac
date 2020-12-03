# Вывести заголовок wav-файла
# если это не WAV (проверить строковые маркеры), вывести "NO"

import struct
import sys
import os


def pread(f, fmt):
    return struct.unpack(fmt, f.read(struct.calcsize(fmt)))[0]


L, B, S = "H", "I", "4s"
name = input()
seekarr = [4, 20, 22, 24, 34, 40]
fmtarr = [B, L, L, B, L, B]
resarr = [0, 0, 0, 0, 0, 0]
marks = [b"RIFF", b"WAVE", b"fmt ", b"data"]
seekm = [0, 8, 12, 36]
if (os.path.getsize(name) > 44) and (name.endswith(".wav")):
    F = open(name, "rb")
    for i in range(6):
        F.seek(seekarr[i])
        resarr[i] = pread(F, fmtarr[i])
    for i in range(4):
        F.seek(seekm[i])
        t = pread(F, S)
        l = marks[i]
        if t != l:
            print("NO")
            sys.exit()
    print("Size={0}, Type={1}, Channels={2}, Rate={3}, Bits={4}, Data size={5}".format(resarr[0], resarr[1],
                                                                                       resarr[2], resarr[3], resarr[4],
                                                                                       resarr[5]))
    F.close()
else:
    print("NO")
