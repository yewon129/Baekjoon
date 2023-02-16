for _ in range(10):
  tc = int(input())
  lst = list(map(int, input().split()))
  
  n = 1
  while lst[-1] != 0:
    if n % 5 == 0:
      num = lst[0] - 5
    else:
      num = lst[0] - n%5
    if num < 0:
      num = 0
    lst.pop(0)
    lst.append(num)
    n += 1

  print(f'#{tc}', end=' ')
  for i in range(len(lst)):
    print(lst[i], end=' ')
  print()
