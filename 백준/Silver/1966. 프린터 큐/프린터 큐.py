T = int(input())

for tc in range(T):
  N, M = map(int,input().split())
  lst = list(map(int, input().split()))

  cnt = 0
  while lst:
    maxV = max(lst)
    front = lst.pop(0)
    M -= 1

    if maxV == front:
      cnt += 1
      if M < 0:
        print(cnt)
        break
    
    else:
      lst.append(front)
      if M < 0:
        M = len(lst) - 1