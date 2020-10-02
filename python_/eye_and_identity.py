import numpy as np
n = tuple(map(int, input().split()))
#x = np.identity(n[0], n[1])
x = np.eye(n[0], n[1])
print(x)


