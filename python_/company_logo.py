# verilen string kendini tekrar eden harflerin kaç tane olduğunu yaz

from collections import Counter as cnt

s = sorted(input())

count = cnt(s).most_common()
#print(count)

count = sorted(count, key=lambda x: (x[1] * -1, x[0]))
for i in range(0, 3):
    print(count[i][0], count[i][1])


"""
from string import ascii_letters as alp
from collections import Counter as cnt

d = {}

s = str(input())
for key, val in cnt(s).items():
    if val == 1:
        pass
    else:
        d[key] = val

for i in d:
    print(i, d[i])
    
"""
