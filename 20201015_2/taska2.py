import sys
import random

a,b,c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
if len(sys.argv)>4:
    random.seed(sys.argv[4])
else:
    s = random.randrange(100500)
    print(f'seed: {s}', file = stderr)
print(*(random.randint(a,b) for i in range(c)))
