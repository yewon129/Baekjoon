T = int(input())

for tc in range(1, T+1):
  N = int(input())
  arr = [list(map(int, input())) for _ in range(N)]

  cnt = 0
  s, e = N//2, N//2
  for i in range(N):
    for j in range(s,e+1):
      cnt += arr[i][j]
    if i < N//2:
      s -= 1
      e += 1
    else:
      s += 1
      e -= 1
  
  print(f'#{tc} {cnt}')