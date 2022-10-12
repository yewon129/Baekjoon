A = int(input())
lst = list(map(int, input().split()))
dp = [0 for _ in range(A)]
for i in range(A):
    for j in range(i):
        if lst[i] > lst[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))