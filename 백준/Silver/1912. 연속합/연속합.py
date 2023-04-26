N = int(input())
lst = list(map(int, input().split()))
dp = [0] * N
dp[N-1] = lst[N-1]
for i in range(N-2, -1, -1):
    dp[i] = max(lst[i], lst[i]+dp[i+1])

print(max(dp))