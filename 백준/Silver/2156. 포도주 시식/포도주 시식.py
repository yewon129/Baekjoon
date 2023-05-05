N = int(input())
lst = [int(input()) for _ in range(N)]

if N == 1:
    print(lst[0])
elif N == 2:
    print(lst[0]+lst[1])
else:
    dp = [0] * (N+1)
    dp[0] = lst[0]
    dp[1] = lst[0]+lst[1]
    dp[2] = max(lst[0]+lst[2], lst[1]+lst[2], dp[1])
    for i in range(3,N):
        dp[i] = max(dp[i-2]+lst[i],dp[i-3]+lst[i]+lst[i-1],dp[i-1])
    
    print(max(dp))