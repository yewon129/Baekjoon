def fn(idx, score, cal):
  global maxV
  if cal > kcal:
    return
  if score > maxV:
    maxV = score
  if idx == N:
    return
  fn(idx+1, score, cal)
  fn(idx+1, score+arr[idx][0], cal+arr[idx][1])

T = int(input())

for tc in range(1, T+1):
  N, kcal = map(int, input().split())
  arr = [list(map(int, input().split())) for _ in range(N)]

  arr.sort(reverse=True)
  maxV = 0
  
  fn(0, 0, 0)
  print(f'#{tc} {maxV}')