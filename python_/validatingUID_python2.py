import re

for i in range(int(raw_input())):
    N = raw_input().strip()
    if N.isalnum() and len(N) == 10:
        if bool(re.search(r'(.*[A-Z]){2,}',N)) and bool(re.search(r'(.*[0-9]){3,}',N)):
            if re.search(r'.*(.).*\1+.*',N):
                print 'Invalid'
            else:
                print 'Valid'
        else:
            print 'Invalid'
    else:
        print 'Invalid'import re
"""
line = int(input())

#pattern = r'^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$'
score = 0
num = 0

for _ in range(line):
    x = list(input())
    x = list([i for i in x])

    for i in x:
        if any(i.isupper()):
            score += 1

        if i.isnumeric():
            score += 1
            num += 1

        if i.isalnum():
            score += 1

    if len(x) == set(x):
        score += 1

    if len(x) == 10:
        score += 1


    print(score)
"""
