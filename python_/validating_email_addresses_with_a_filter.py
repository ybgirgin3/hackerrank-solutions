import re
def fun(s):
    #pattern = r'^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$'

    emailed = []

    regex = '^[\w-]+@[a-zA-Z\d]+\..{,3}$'
    if bool(re.match(regex, s)):
        emailed.append(s)
    else:
        return []


    return sorted(emailed)

    

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


"""
n = int(input())
emails = [input() for _ in range(n)]
print(sorted(emails)
"""
