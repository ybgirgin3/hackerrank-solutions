x = input()
f = set(map(int, input().split()))

y = input()
s = set(map(int, input().split()))


ret = f.symmetric_difference(s)
#print(ret)
print(len(list(ret)))


