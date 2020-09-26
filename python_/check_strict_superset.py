# ters işlem yapılaca
# super set olan bulunabiliyor fakat strict superset onun tam tersi oluyor

"""

A = set(map(int, input().split()))
c = int(input())
for _ in range(c):
    other = set(map(int, input().split()))

    if not A.issuperset(A) or len(A) == len(other):
        print('False')
        break
    else: print('True')


"""
A = set(map(int, input().split()))
count_sets = int(input())
other_one = set(map(int, input().split()))
other_two = set(map(int, input().split()))

if (A.issuperset(other_one) and A.issuperset(other_two)) or (len(A) == len(other_one) or len(A) == len(other_two)):
    print('True')
else:
    print('False')

