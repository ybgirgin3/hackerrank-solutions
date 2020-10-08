import re

n = int(input())
reg = '[789]\d{9}$'
for _ in range(n):
    if re.match(reg, input()):
        print('YES')
    else:
        print('NO')
