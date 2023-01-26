N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
box = []

def dfs(st):
  if len(box) == M:
    print(*box)
    return
  for i in range(st, N):
    if lst[i] not in box:
      box.append(lst[i])
      dfs(i+1)
      box.pop()

dfs(0)