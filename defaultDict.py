from collections import defaultdict
# input
# first line contains integers, n and m seperated by a space
# the next n lines contains the words belonging to group A
# the next m lines contains the words belonging to group B

# A listesi
A = []

# B listesi
B = []

# take first integers m and n
m, n = map(int, input().split())

# elemanları al
A = [input() for _ in range(m)]
B = [input() for _ in range(n)]

d = defaultdict(list)
index = 0
for i in A:
    d[i].append(A.index(i, index) + 1)
    index += 1

for i in B:
    if i not in A:
        print(-1)
    else:
        print(" ".join(map(str, d[i])))
