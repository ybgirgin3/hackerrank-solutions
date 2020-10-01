import numpy as np
np.set_printoptions(sign=' ')

n, m = input().split()
arr = np.array([input().split() for _ in range(int(n))], int)

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(np.around(np.std(arr), decimals=12))
