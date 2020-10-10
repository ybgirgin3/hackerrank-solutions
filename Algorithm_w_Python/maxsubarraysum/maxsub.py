#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumSum function below.
def divider(a, dat):
    pass




def maximumSum(a, m):
    # ilk sayı 1 tane liste gireceğimizi gösteriyor
    # ikinci satırdaki ilk sayı kaç elemanlı bir liste olacağını
    # ikinci satırdaki ikinci sayı ise kaça böleceğimizi gösteriyor
    # elemanları böldükten sonra en büyük olanı ise ekrana döndürüyoruz

    # a bir liste
    # a daki her bir elemanı ekrana bir defa yazdır - iki tane olanları bile

    # find duplicated items and make a list with them
    _size = len(a)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if a[i] == a[j] and a[i] not in repeated:
                repeated.append(a[i])
                a.remove(a[i])
    # divider(repeated)
    print(repeated)
    print(a)





if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)



