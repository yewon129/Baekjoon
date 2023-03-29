N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

def bfs(sti, stj):
    queue = [(sti, stj)]
    visited[sti][stj] = 1
    cnt = 1
    while queue:
        i, j = queue.pop(0)
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                queue.append((ni,nj))
                visited[ni][nj] = 1
                cnt += 1
    return cnt
box = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            box.append(bfs(i, j))

box.sort()
print(len(box))
for i in box:
    print(i)