
from collections import OrderedDict

# define dict
goodies = OrderedDict()

N = int(input())

for _ in range(N):
    item = input().split()
    name = ' '.join(item[:-1])

    if name in goodies:
        goodies[name] += int(item.pop())
    else:
        goodies[name] = int(item.pop())


for i in goodies:
    print("%s %d" % (i, goodies[i]))




"""
d = od()

# number of items
N = int(input())


for _ in range(N):
    n = input().strip().split()
    name = ' '.join(n[:-1])
    for name in d:
        d[name] += int(n.pop())
    else:
        d[name] = int(n.pop())

for i in d:
    print("%s %d" % i, d[i])
    
"""
