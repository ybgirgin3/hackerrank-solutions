x = input()
f = set(map(int, input().split()))

y = input()
s = set(map(int, input().split()))


ret = f.intersection(s)
print(len(list(ret)))


