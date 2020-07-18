#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    atot = 0
    btot = 0
    # ret = [i == j for i, j in zip(a, b) if ]

    # iki listedeki aynı indexteki elemanlarını karşılaştır büyük olana 1 yaz

    for i, j in zip(a, b):
        if i > j:
            atot += 1
        elif i < j:
            btot += 1
        else: pass

    print(atot, btot)


    
if __name__ == '__main__':

    # ikisinde liste bunların
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

