import re

T = int(input())
l = []

for _ in range(T):
    try:
        reg = input()
        re.compile(reg)
        isValid = True
        l.append(isValid)
    except re.error:
        isValid = False
        l.append(isValid)

for i in l:
    print(i)
