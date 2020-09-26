# n tane integer içeren array var
# ve iki tane birbiri ile bağlantısı olmayan setler: A ve B
# setlerin herbiri m tane integer içeriyor
# ilk mutluluk 0
# A setindeki integerları seviyorsun
# B setindeki integerları sevmiyorsun
# eğer içindeki herbir eleman eğer A setinin elemanı ise mutluluğa 1 ekleyeceksin
# eğer B setinin elemanı ise mutluluğa -1 ekleyeceksin
# eğer ikisindende de yoksa mutluluğunda herhangi bir değişiklik olmayacak

# NOTE: A ve B set olduklarından dolayı tekrar eden elemanları yok. ama bu arrayin iki tane aynı elemanı içeremeyeceği anlamına gelmiyor

len_array, sets_count = input().split()
array = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happ = 0

for i in array:
    if (i in A) and (i not in B):
        happ += 1
    elif (i in B) and (i not in A):
        happ -= 1
    else:
        pass



print(happ)
