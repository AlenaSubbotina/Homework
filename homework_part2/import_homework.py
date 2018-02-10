import datetime

year, month, day = map(int, input().split())
days = int(input())

mydate = datetime.date(year, month, day)

delta = datetime.timedelta(days)

mynewdate = mydate + delta

print(mynewdate.year, mynewdate.month, mynewdate.day)
