import re
import email.utils

n = int(input())

pattern = r'^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$'

for _ in range(n):
    parsed = email.utils.parseaddr(input())
    if re.search(pattern, parsed[1]):
        print(email.utils.formataddr(parsed))

