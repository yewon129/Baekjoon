T = int(input())

for tc in range(1, T+1):
  N = int(input())
  lst = list(map(int, input().split()))
  answer = 0
  while 1:
    idx = lst.index(max(lst))
    if idx == 0 and len(lst) > 1:
      lst.pop(0)
    elif idx == 0:
      break
    else:
      answer += idx * lst[idx] - sum(lst[:idx])
      lst = lst[idx+1:]
    if len(lst) <= 1:
      break

  print(f'#{tc} {answer}')