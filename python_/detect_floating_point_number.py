import re
n = int(input())

inputs = [input() for _ in range(n)]
for s in inputs:
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', s)))

