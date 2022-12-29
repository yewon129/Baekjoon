def factorial(n):
  if n == 0:
    return 1
  else:
    return factorial(n-1) * n

N = int(input())
lst = [0]*21
cnt = 0
num = 0

for i in range(21):
  lst[i] = factorial(i)

if N == 0:
  print('NO')
else:
  for i in range(20, -1, -1):
    if N < lst[i]:
      pass
    else:
      N -= lst[i]
    if N == 0:
      break
  if N == 0:
    print('YES')
  else:
    print('NO')