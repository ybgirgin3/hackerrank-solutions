from collections import deque

d = deque()


n = int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'append':
        d.append(int(cmd[1]))

    if cmd[0] == 'appendleft':
        d.appendleft(int(cmd[1]))

    if cmd[0] == 'pop':
        d.pop()

    if cmd[0] == 'popleft':
        d.popleft()


#print(d)
d = list(d)
for i in d:
    print(i, end = " ")

