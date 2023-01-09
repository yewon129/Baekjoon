N = int(input())
lst = [int(input()) for _ in range(N)]

lst.sort()

maxV = 0
for i in range(N):
  cnt = lst[i] * (N-i)
  if maxV < cnt:
    maxV = cnt


print(maxV)