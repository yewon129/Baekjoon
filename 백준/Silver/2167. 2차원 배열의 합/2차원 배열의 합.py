N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    ans = 0
    for n in range(i-1, x):
        for m in range(j-1, y):
            ans += arr[n][m]
    print(ans)
