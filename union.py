x = int(input())
f = set(map(int, input().split()))

y = int(input())
s = set(map(int, input().split()))


ret = f.union(s)
print(len(list(ret)))
