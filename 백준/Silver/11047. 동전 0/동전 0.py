N, K = map(int, input().split())
lst = list(int(input()) for _ in range(N))

cnt = 0
for i in reversed(range(N)):
    cnt += K//lst[i]
    K %= lst[i]

print(cnt)