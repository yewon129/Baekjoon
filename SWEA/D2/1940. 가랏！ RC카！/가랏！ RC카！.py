T = int(input())

for tc in range(1, T+1):
  N = int(input())
  v = 0
  l = 0
  for _ in range(N):
    lst = list(map(int, input().split()))
    if len(lst) == 1:
      l += v
    elif lst[0] == 1:
      v += lst[1]
      l += v
    elif lst[0] == 2:
      v -= lst[1]
      if v < 0:
        v = 0
      l += v
  print(f'#{tc} {l}')
