N = int(input())
lst = list(map(int, input().split()))
a = int(input())

cnt = 0
for i in range(N):
    if lst[i] == a:
        cnt += 1

print(cnt)