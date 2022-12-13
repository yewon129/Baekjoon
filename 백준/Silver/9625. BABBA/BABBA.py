dp = [0, 1]
n = int(input())
while(n+1 > len(dp)):
    dp.append(dp[-1] + dp[-2])
print(dp[-2], dp[-1])