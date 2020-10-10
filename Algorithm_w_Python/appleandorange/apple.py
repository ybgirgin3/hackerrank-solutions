#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # elma ve portakalın düştüğü eksen değerlerini ağaçların olduğu eksen değeri ile topluyoruz ve oluşan listelerin içinde 7 ile 10 arasında kaç tane eleman varsa ona göre değer döndürüyoruz
    # print(s, t, a, b, apples, oranges) 
    appleCnt = 0
    orangCnt = 0
    # find apples
    # iki ağacın arasında a ve b nereye düştüğünün lokasyonlarını bulmak lazım
    for apple in apples:
        loc = a + apple
        # print('apple loc: ', loc)
        if loc in range(s, t+1):
            appleCnt += 1
            print(appleCnt)

    for orange in oranges:
        loc = b + orange
        # print('orange loc: ', loc)
        if loc in range(s, t+1):
            orangCnt += 1
            print(orangCnt)


    # print(appleCnt, orangCnt)








   



if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

