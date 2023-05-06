def solution(land):
    answer = 0
    N = len(land)
    dp =[[0] * 4 for _ in range(N)]
    for j in range(4):
        dp[0][j] = land[0][j]
    for i in range(1,N):
        for j in range(4):
            for k in range(4):
                if k != j:
                    dp[i][j] = max(dp[i-1][k]+land[i][j], dp[i][j])
    
    answer = max(dp[-1])
    return answer