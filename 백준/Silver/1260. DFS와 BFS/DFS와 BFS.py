from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
v = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

def dfs(s):
    print(s, end=' ')
    v[s] = 1
    for i in graph[s]:
        if v[i] == 0:
            dfs(i)
            v[i] = 1

def bfs(s):
    q=deque([s])
    v[s] = 1
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if v[i] == 0:
                q.append(i)
                v[i] =1

dfs(V)
v = [0] * (N+1)
print()
bfs(V)