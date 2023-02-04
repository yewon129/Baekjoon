N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = []
for i in range(N):
  dp.append(lst[i][1])
dp.append(0)

for i in range(N-1, -1, -1):
  if lst[i][0] + i > N:
    dp[i] = dp[i+1]
  else:
    dp[i] = max(dp[i+1], lst[i][1] + dp[i+ lst[i][0]])

print(dp[0])