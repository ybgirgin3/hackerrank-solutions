import numpy as np

n,m = input().split()

arr = np.array([input().split() for _ in range(int(n))], int)
mins = list(np.min(arr, axis=1))
#print(type(mins))

print(min([min_ for min_ in mins if min_ != 0]))
print(max(mins))

