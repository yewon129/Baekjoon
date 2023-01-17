for _ in range(3):
  N = int(input())
  lst = [int(input()) for _ in range(N)]
  V = sum(lst)
  if V < 0:
    print('-')
  elif V == 0:
    print(0)
  else:
    print('+')