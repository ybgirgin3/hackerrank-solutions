import sys
import numpy as np
# np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(suppress=True)


arr = np.array([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])

# print(type(arr))
maxIt = np.where(arr == np.amax(arr))

# print(maxIt[0])

res = ' '.join(map(str, maxIt[0]))
print(res)



