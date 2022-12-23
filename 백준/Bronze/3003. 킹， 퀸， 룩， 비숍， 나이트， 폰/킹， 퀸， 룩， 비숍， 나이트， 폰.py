lst = list(map(int, input().split()))

ans = [0] * 6
for i in range(6):
    if i == 1 or i == 0:
        ans[i] = 1 - lst[i]
    elif i == 2 or i == 3 or i == 4:
        ans[i] = 2 - lst[i]
    elif i == 5:
        ans[i] = 8 - lst[i]
 
for j in range(6):
    print(ans[j], end=' ')