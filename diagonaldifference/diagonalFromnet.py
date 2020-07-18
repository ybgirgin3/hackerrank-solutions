# bir tane matris verilecek onun soldan çapraz elemanlarını topla
# daha sonra sağdan sola olan elemanlarını topla
# mutlak farklarını döndür

#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    f = 0 # aka first
    s = 0 # aka second
    lenght = len(arr[0])
    print(lenght)

    for i in range(lenght):
        f += arr[i][i]
        s += arr[i][(lenght-i-1)]
    return abs(f-s)



if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
