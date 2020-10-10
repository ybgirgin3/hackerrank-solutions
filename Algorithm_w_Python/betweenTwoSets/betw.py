#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # ilk girilen ikilinin tam olarak böldüğü sayılar eğer sonraki girilen 3'lüyü de bölmesi gerekiyor
    # dönebilen sayıların sayısını döndür
    # print('a', a) # ilk girilen ikili
    # print('b', b) # ikinci olarak girilen üçlü
    f = []
    s = []
    t = 0
    # print(b[-1])  # returns 96

    # TODO:
    # birinci girdiğinin ikincinin birinci değerine kadar olan sayılardan hangilerine tam olarak bölündüğünü bul
    # daha sonra o sayılardan hangilerinin ikincinin elemanlarının hepsine bölündüğünü bul
    # ve onların sayılarını döndür

    for i in range(b[0]+1):
        for x in a:
            if i % x == 0:
                f.append(i)

    # ikisinde bölünmeyenleri yolla
    for i in f:
        for x in a:
            if i % x != 0:
                f.remove(i)


    # iki tane olanları teke düşür

    # print(f)
    # set liste içinde iki tane olanları çıkarıyor
    f = list(set(f))
    # print(list(set(f)))

    # ikinci liste üzerinde işlem yap
    for i in b:
        for x in f:
            if x == 0:
                pass
            else:
                if i % x == 0:
                    s.append(x)



    for i in b:
        for x in s:
            if i % x != 0:
                s.remove(x)


    p = list(set(s))
    print(len(p))



     

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)



