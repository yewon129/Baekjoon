N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.insert(0, [0,0])
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        w = arr[i][0]
        v = arr[i][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])

print(dp[N][K])