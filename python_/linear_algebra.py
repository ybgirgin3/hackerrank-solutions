import numpy

n = int(input())
arr = numpy.array( [(list((map(float, input().split())))) for i in range(n)] )
s = numpy.linalg.det(arr)
print(round(s, 2))

