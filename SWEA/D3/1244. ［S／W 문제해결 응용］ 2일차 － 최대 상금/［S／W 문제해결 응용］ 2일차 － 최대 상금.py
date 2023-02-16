T = int(input())

for tc in range(1, T+1):
  num, N = input().split()
  N = int(N)
  n = len(num)
  number = set([num])
  box = set()

  for i in range(N):
    while number:
      s = number.pop()
      s = list(s)
      for l in range(n):
        for m in range(l+1, n):
          s[l], s[m] = s[m], s[l]
          box.add(''.join(s))
          s[l], s[m] = s[m], s[l]
    number, box = box, number
  
  print('#{} {}'.format(tc, max(map(int, number))))