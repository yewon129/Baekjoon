N = int(input())
M = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    arr[x][y] = y
    arr[y][x] = x

cnt = 0
visited = [0] * (N+1)

def dfs(start):
    global cnt
    visited[start] = 1
    for i in arr[start]:
        if i != 0 and visited[i] == 0:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)