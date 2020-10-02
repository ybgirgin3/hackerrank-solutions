import numpy as np
n,m = map(int, input().split())

arr = np.array( [list(map(int, input().split())) for _ in range(m)] )

print(arr.T)
#print(arr.flatten)
print(arr.flatten())
