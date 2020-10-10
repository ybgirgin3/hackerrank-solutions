# her öğrenci 0 ile 100 arasında not alır
# 40'dan düşük olan notlar kalır

# sam her öğrencinin notlarının şu kurallara göre yuvarlıyor
    # eğer not ile 5'in bir sonraki katı arasındaki fark 3'ten az ise, notu 5'in katına yuvarla
    # eğer not 38'den az ise yuvarlama yapmıyor not direk kalıyor




#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # 5'in katlarının olduğu bir liste olur 
    # o listede hangi elemanların bundan büyük olduğunu buldururum
    # farklarının alırım farkın en küçük olduğu sayıyı ise 5'in bir sonraki katı seçerim

    print('--------')
    for i in range(len(grades)):
        if grades[i] > 37:
            if (5 - (grades[i] % 5)) < 3:
                grades[i] += (5 - (grades[i] % 5))
    print(grades)




if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)


