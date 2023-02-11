T = int(input())
for tc in range(1, T+1):
  lst = list(map(str, input()))
  box = []
  flag = 0

  for i in range(len(lst)):
    if flag == 1:
      break
    if len(box) == 0:
      box.append(lst[i])
    else:
      if lst[i] == box[0]:
        for j in range(len(box)):
          if lst[i+j] == box[j]:
            if j == len(box)-1:
              flag = 1
          else:
            box.append(lst[i])
            break
      else:
        box.append(lst[i])
    
  print(f'#{tc} {len(box)}')