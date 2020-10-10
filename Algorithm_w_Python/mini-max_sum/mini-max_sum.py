#!/bin/python3

# girilen 5 tane integer'in 4 tanesini topla daha sonra bu toplamların en büyük ve en küçük olanını ekrana yazdır
import math
import os
import random
import re
import sys
from functools import reduce

# Complete the miniMaxSum function below.
minList = []
maxList = []
def miniMaxSum(arr):
    # remove komutunu kullan
    k = min(arr)
    b = max(arr)
    # en küçük olan çıkar geri kalanı topla
    arr.remove(k)
    bigSum = reduce(lambda x,y : x+y, arr)
    

    # en küçük olan ekle
    arr.append(k)
    arr.remove(b)
    litSum = reduce(lambda x,y : x+y, arr)

    print(litSum, bigSum)








if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

