N = int(input())
lst = list(map(int, input().split()))
x = int(input())
lst.sort()

cnt = 0
for i in range(N-1):
    if lst[i] > x:
        break
    for j in range(i+1, N):
        if lst[i] + lst[j] == x:
            cnt += 1
            break
        elif lst[i] + lst[j] > x:
            break

print(cnt)