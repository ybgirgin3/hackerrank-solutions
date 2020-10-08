import re

str_ = str(input())
ref = str(input())

pattern = re.compile(ref)

mtc = pattern.search(str_)

if not mtc:
    print('(-1, -1)')
while mtc:
    print('({0}, {1})'.format(mtc.start(), mtc.end() - 1 ))
    mtc = pattern.search(str_, mtc.start() + 1)

