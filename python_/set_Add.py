n = int(input())

countr = []

for _ in range(n):
    countr.append(input())

#print(countr)
print(len(list(set(countr))))
