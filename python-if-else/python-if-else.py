#!/bin/python3

import math
import os
import random
import re
import sys


def x(n):
    if n % 2 != 0:
        print('Weird')
    if n % 2 == 0:
        if n in range(2, 6):
            print('Not Weird')
        elif n in range(6, 21):
            print('Weird')
        elif n > 20:
            print('Not Weird')




if __name__ == '__main__':
    n = int(input().strip())
    x(n)

