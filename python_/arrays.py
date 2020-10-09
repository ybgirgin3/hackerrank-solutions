import numpy

def arrays(arr):
  arr = numpy.array(arr, float)
  return arr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
