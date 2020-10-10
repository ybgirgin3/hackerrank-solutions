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
    # print(arr)
    # arr değişkeni içinde 3 eleman içeren 3 tane liste olarak dönüyor
    flist = []
    slist = []
    ind = 0
    ind2 = 2
    for i in arr:
        # hepsini ortasındaki elemanı yazıyor
        # print(i[ind])
        flist.append(i[ind])
        ind += 1

    for x in arr:
        slist.append(x[ind2])
        # print(x[ind2])
        ind2 -= 1


    # listeleri topla
    fret = reduce(lambda x,y: x+y, flist)
    sret = reduce(lambda x,y: x+y, slist)

    abssum = abs(fret - sret)
    print(abssum)




if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
