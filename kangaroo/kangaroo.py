#!/bin/python3

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
        #The case of same speed
    if v1 == v2 and x1 == x2:
        print('YES')
    elif v1 == v2:
        print('NO')

    x = (x2-x1) / (v1-v2)
    if (x == round(x) and x > 0):
        print('YES')
    else:
        print('NO')



if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)



