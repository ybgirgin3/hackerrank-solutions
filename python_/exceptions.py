x = int(input())

lst = []

for _ in range(x):
    try:
        f, s = map(int, input().split())
        ret = f // s
        lst.append(ret)
    except ZeroDivisionError as e:
        ret = "Error Code: {}".format(e)
        lst.append(ret)
    except ValueError as e:
        ret = "Error Code: {}".format(e)
        lst.append(ret)


for i in lst:
    print(i)
