def solution(elements):
    answer = 0
    N = len(elements)
    box = [0] * (2*N)
    for i in range(N):
        box[i] = elements[i]
        box[N+i] = elements[i]
    dp = [0] * (2*N)
    dp[0] = elements[0]
    for i in range(1, 2*N):
        dp[i] = dp[i-1] + elements[i%N]
    dp = [0] + dp

    temp = []
    for l in range(1, N+1):
        for i in range(l,N+l):
            temp.append(dp[i] - dp[i-l])
            
    answer += len(list(set(temp)))
    
    
    return answer