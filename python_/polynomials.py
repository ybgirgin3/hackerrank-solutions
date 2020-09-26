import numpy

coeff = list(map(float, input().split()))
x = float(input())


print(numpy.polyval(coeff, x))
