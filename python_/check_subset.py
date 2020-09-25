l = []

test_case = int(input())

for _ in range(test_case):
    a_times = int(input())
    A = set(map(int, input().split()))

    b_times = int(input())
    B = set(map(int, input().split()))

    #print(A.issubset(B))
    l.append(A.issubset(B))




for i in l:
    print(i)

