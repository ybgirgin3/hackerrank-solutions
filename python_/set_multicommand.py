x = int(input())
# set items
s = set(map(int, input().split()))

y = int(input())

for _ in range(y):
    cmd = input().split()
    if cmd[0] == 'remove':
        s.remove(int(cmd[1]))
    elif cmd[0] == 'discard':
        s.discard(int(cmd[1]))
    elif cmd[0] == 'pop':
        s.pop()


print(sum(list(s)))
