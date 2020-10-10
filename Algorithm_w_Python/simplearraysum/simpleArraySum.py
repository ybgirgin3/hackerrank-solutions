#!/bin/python3

import os
import sys
from functools import reduce

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    ret = reduce(lambda x, y : x + y, ar)
    return ret

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)



