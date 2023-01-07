N ,M = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0
for i in range(N):
  cnt = 0
  j = 0
  while i+j<N and cnt <= M:
    if i+j >= N:
      break
    cnt += lst[i+j]
    if cnt == M:
      ans += 1
      break
    j += 1

print(ans)