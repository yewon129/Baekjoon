T = int(input())

def bfs(i, j):
    global v
    q = []
    q.append([i,j])
    v[i][j] = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[0,1], [1,0], [0,-1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<M and 0<= nj < N and arr[ni][nj] == 1 and v[ni][nj] == 0:
                q.append([ni,nj])
                v[ni][nj] = 1

for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * N for _ in range(M)]
    for k in range(K):
        x, y = map(int, input().split())
        arr[x][y] = 1

    cnt = 0
    v = [[0] * N for k in range(M)]
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1 and v[i][j] == 0:
                cnt += 1
                bfs(i,j)

    print(cnt)
