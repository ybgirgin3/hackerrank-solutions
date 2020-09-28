import numpy as np

a = np.array([input().split()], int)
b = np.array([input().split()], int)
print(int(np.inner(a,b)))
print(np.outer(a,b))

