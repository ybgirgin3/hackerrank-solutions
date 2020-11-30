#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
  pass



if __name__ == '__main__':

  nk = input().split()

  n = int(nk[0])

  k = int(nk[1])

  ar = list(map(int, input().rstrip().split()))

  result = divisibleSumPairs(n, k, ar)
