#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
nList = []
pList = []
zList = []


def divider(z, n, p, h):
    pos = p / h
    neg = n / h
    zer = z / h
    # print('{}\n{}\n{}\n'.format(pos, neg, zer))
    print('%.6f\n%.6f\n%.6f' % (pos, neg, zer))



def plusMinus(arr, h):
    # print(arr)
    for i in arr:
        if i == 0:
            zList.append(0)

        elif i < 0:
            nList.append(i)

        elif i > 0:
            pList.append(i)


    divider(len(zList), len(nList), len(pList), h)




if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)

