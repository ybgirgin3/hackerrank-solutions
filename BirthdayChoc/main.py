#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    # s: an array of integers, the numbers on each of the squares of chocolate
    # d: an integer, Ron's birth day
    # m: an integer, Ron's birth month
    pass



if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)


