lst = list(map(int, input().split()))

cnt = 0
for a in lst:
    cnt += a**2
    
print(cnt % 10)