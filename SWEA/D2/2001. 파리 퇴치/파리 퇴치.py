T = int(input())
for tc in range(1, T+1):
  N, M = map(int, input().split())
  arr = [list(map(int, input().split())) for _ in range(N)]

  maxV = 0
  for i in range(N-M+1):
    for j in range(N-M+1):
      cnt = 0
      for k in range(M):
        for l in range(M):
          cnt += arr[i+k][j+l]
      if cnt > maxV:
        maxV = cnt
  
  print(f'#{tc} {maxV}')