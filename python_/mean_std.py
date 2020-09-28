import numpy as np

n, m = input().split()
arr = np.array([input().split() for _ in range(int(n))], int)

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
x = np.std(arr)
print(round(x, 11))


