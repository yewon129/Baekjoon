from itertools import permutations

N = int(input())
lst = list(map(int, input().split()))
cal = list(map(int, input().split()))
box = []
for i in range(4):
  for j in range(cal[i]):
    box.append(i)

calculation = list(set(list(permutations(box,N-1))))
minV = 10000000000
maxV = -10000000000
for i in range(len(calculation)):
  cnt = lst[0]
  for j in range(N-1):
    if calculation[i][j] == 0:
      cnt += lst[j+1]
    elif calculation[i][j] == 1:
      cnt -= lst[j+1]
    elif calculation[i][j] == 2:
      cnt *= lst[j+1]
    else:
      if cnt < 0:
        cnt *= -1
        cnt //= lst[j+1]
        cnt *= -1
      else:
        cnt //= lst[j+1]
  if cnt > maxV:
    maxV = cnt
  if cnt < minV:
    minV = cnt

print(maxV)
print(minV)