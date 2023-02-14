T = int(input())

for tc in range(1, T+1):
  arr = [list(map(int, input().split())) for _ in range(9)]

  flag = 0
  for i in range(9):
    if flag == 1:
      break
    cnt_1 = 0
    cnt_2 = 0
    for j in range(9):
      cnt_1 += arr[i][j]
      cnt_2 += arr[j][i]
    if cnt_1 != 45 or cnt_2 != 45:
      flag = 1
    
  for i in [0, 3, 6]:
    for j in [0, 3, 6]:
      if flag == 1:
        break
      cnt = 0
      for m in range(3):
        for n in range(3):
          cnt += arr[i+m][j+n]
      if cnt != 45:
        flag = 1
                
  if flag == 1:
    print(f'#{tc} 0')
  else:
    print(f'#{tc} 1')