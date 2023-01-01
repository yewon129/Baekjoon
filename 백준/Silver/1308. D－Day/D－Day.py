import datetime

date = list(map(int, input().split()))
dday = list(map(int, input().split()))

start = datetime.date(date[0], date[1], date[2])
start_1000 = datetime.date(date[0]+1000, date[1], date[2])
end = datetime.date(dday[0], dday[1], dday[2])

result_1000 = start_1000 - start
result = end - start
if result < result_1000:
  print(f"D-{result.days}")
else:
  print("gg")