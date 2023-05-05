N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]

for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1,x2):
        for j in range(y1, y2):
            arr[i][j] += 1

v = [[0]*M for _ in range(N)]
def bfs(i, j):
    q = [[i,j]]
    v[i][j] = 1
    cnt = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0 and v[ni][nj] == 0:
                q.append([ni,nj])
                v[ni][nj] = v[i][j] + 1
                cnt += 1
    return cnt

answer = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and v[i][j] == 0:
            answer.append(bfs(i,j))

print(len(answer))
answer.sort()
print(*answer)