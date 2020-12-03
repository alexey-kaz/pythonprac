import sys

file_in = sys.stdin.buffer
file_out = sys.stdout.buffer
N = file_in.read(1)
file_out.write(N)
N = int(N[0])
data = b"".join(line.strip() for line in file_in)
for i in sorted(data[i*len(data)//N:(i+1)*len(data)//N] for i in range(N)):
    file_out.write(i)
