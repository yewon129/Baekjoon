N = int(input())

lst = [0]*N
for i in range(N):
  name, k, e, m = map(str, input().split())
  lst[i] = [name, int(k), int(e), int(m)]

lst.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(N):
  print(lst[i][0])