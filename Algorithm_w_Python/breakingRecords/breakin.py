#!/usr/bin/python3

### çalışmıyor aq

import math
import os
import random
import re
import sys
import numpy as np
np.set_printoptions(suppress=True)


# Complete the breakingRecords function below.
def breakingRecords(scores):
    # n tane sayı girilecek
    # girilen sayıların max ve min terimlerinin
    # hangi indexte olduğunu ekrana dönmek gerek
    # print(type(scores))




    # turn list to np array
    arr = np.array(scores)

    # find max ind
    # maxEL = np.amax(arr)

    # find min ind
    # minEL = np.amin(arr)

    # finds elements 
    # print(maxEL, minEL)

    maxRes = np.where(arr == np.amax(arr))
    minRes = np.where(arr == np.amin(arr))

    # prints (array([9]),) (array([0]),)
    # which is true but not wanted
    # print(maxRes, minRes)

    maxIt = ' '.join(map(str, maxRes[0]))
    minIt = ' '.join(map(str, minRes[0]))

    print(maxIt, minIt)



if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

