N, M, V = map(int, input().split())
lst = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[a][b] = b
    lst[b][a] = a

visited = [0] * (N+1)
def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for j in lst[v]:
        if j != 0 and visited[j] == 0:
            dfs(j)

def bfs(v):
    visited = [0] * (N + 1)
    visited[v] = 1
    print(v, end=' ')
    queue = [v]
    while queue:
        k = queue.pop(0)
        for k in lst[k]:
            if k != 0 and visited[k] == 0:
                visited[k] = 1
                queue.append(k)
                print(k, end=' ')

dfs(V)
print()
bfs(V)