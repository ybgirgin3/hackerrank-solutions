import numpy as np
# 3 3 3 girilecek 3x3 olan 3 tane mtx

x = list(map(int, input().split()))

for _ in range(x[2]):
    print()
    print(np.zeros((x[0], x[1])))

for _ in range(x[2]):
    print(np.ones((x[0], x[1])))
    print()

