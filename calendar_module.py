# mm dd yyyy verilecek onun hangi güne denk geldiğini bul

import calendar

# input
mm, dd, yyyy = map(int, input().split())

#print(mm, dd, yyyy)
target = calendar.weekday(yyyy, mm, dd)
ret = calendar.day_name[target].upper()
print(ret)


