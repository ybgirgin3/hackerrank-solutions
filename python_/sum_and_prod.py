import numpy as np

n,m = list(map(int, input().split()))

arr = np.array([input().split() for _ in range(n)], int)

sum_ = np.sum(arr, axis=0)
print(np.prod(sum_))



