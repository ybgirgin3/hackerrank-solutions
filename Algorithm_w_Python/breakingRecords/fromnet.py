#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxi=scores[0]
    mini=scores[0]
    print(maxi, mini)
    maxcount =0
    mincount=0
    for i in range(len(scores)):
        if(scores[i]>maxi):
            maxi = scores[i]
            maxcount+=1
        if(scores[i]<mini):
            mini = scores[i]
            mincount+=1
    # return [maxcount, mincount]
    # print([maxcount, mincount])

if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
