for _ in range(10):
  tc = int(input())
  arr = [list(map(int, input().split())) for k in range(100)]

  maxV = 0
  for i in range(100):
    cnt_l = 0
    cnt_r = 0
    for j in range(100):
      cnt_l += arr[i][j]
      cnt_r += arr[j][i]
    if cnt_l > maxV:
      maxV = cnt_l
    if cnt_r > maxV:
      maxV = cnt_r
  
  cnt_a = 0
  cnt_b = 0
  for i in range(100):
    cnt_a += arr[i][i]
    cnt_b += arr[99-i][i]
  if cnt_a > maxV:
    maxV = cnt_a
  if cnt_b > maxV:
    maxV = cnt_b
  
  print(f'#{tc} {maxV}')