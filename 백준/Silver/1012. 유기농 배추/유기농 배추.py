def bfs(i,j):
    q = [(i,j)]
    arr[i][j] = 0
    visited = [[0]*M for _ in range(N)]
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j + dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                visited[ni][nj] = 1
                arr[ni][nj] = 0
                q.append((ni,nj))
    return

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())  # M : 가로, N : 세로, K: 개수
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)