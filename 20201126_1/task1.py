import sys
import os

fin = sys.stdin.buffer
fout = sys.stdout.buffer
N = fin.read(1);
fout.write(N);
N = int(N[0]);
data = b"".join(fin.readlines())
L = len(data);
arr = sorted(data[i*L//N:(i+1)*L//N] for i in range(N));
for i in arr:
    fout.write(i);
