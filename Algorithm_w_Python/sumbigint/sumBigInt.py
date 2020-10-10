#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    # bu kodun çok büyük sayıları toplaması lazım
    # daha sonraki değişken ise bir liste olarak dönecek
    ret = reduce(lambda x, y : x+y, ar)
    print(ret)



if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)



