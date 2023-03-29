N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
maxV = max(max(arr))
box = []

def bfs(sti, stj, h):
    queue = [[sti, stj]]
    while queue:
        i, j = queue.pop(0)
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] > h and visited[ni][nj] == 0:
                queue.append([ni,nj])
                visited[ni][nj] = visited[i][j] + 1

for h in range(maxV):
    cnt = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > h and visited[i][j] == 0:
                bfs(i,j,h)
                cnt += 1
    box.append(cnt)

print(max(box))