N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
points = [list(map(int, input().split())) for _ in range(M)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = arr[0][0]

for i in range(N):
    dp[i][0] = arr[i][0]
    for j in range(1, N):
        dp[i][j] = dp[i][j-1] + arr[i][j]
        

for k in range(M):
    x1, y1, x2, y2 = points[k]
    answer = 0
    if y1 != 1:
        for i in range(x1-1, x2):
            answer += dp[i][y2-1] - dp[i][y1-2]
    else:
        for i in range(x1-1, x2):
            answer += dp[i][y2-1]

    print(answer)