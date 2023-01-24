def dfs(node, cnt):
  global visited
  visited[node] = 1
  for n in lst[node]:
    if visited[n] == 0:
      cnt = dfs(n, cnt+1)
  return cnt

T = int(input())

for _ in range(T):
  N, M = map(int, input().split())
  lst = [[] for l in range(N+1)]
  for i in range(M):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)
  
  visited = [0]*(N+1)
  visited[1] = 0
  cnt = dfs(1, 0)

  print(cnt)