x = input()
f = set(map(int, input().split()))

y = input()
s = set(map(int, input().split()))


ret = f.difference(s)
#print(ret)
print(len(list(ret)))


