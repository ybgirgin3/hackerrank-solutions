# find biggest int in list and print how many is there
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    # ar is a list
    print(ar.count(max(ar)))

if __name__ == '__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
