def bfs(N, M):  # N:행, M:열
    visited = [[0]*M for _ in range(N)]  # visited 생성
    q = [0]*(N*M)  # 큐 생성
    cnt = 0
    rear = front = -1
    for i in range(N):  # 시작점 인큐 (익은 토마토가 있는 위치)
        for j in range(M):
            if box[i][j]==1:
                rear += 1
                q[rear] = (i, j)
                # q.append((i,j))
                visited[i][j] = 1  # 시작점 인큐표시
            elif box[i][j] == 0:
                cnt += 1
    if cnt == 0 and len(q) > 0:
        return 0
    while front != rear:
        #i, j = q.pop(0)
        front += 1
        i, j = q[front]
        # visit(i,j)
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and box[ni][nj] == 0 and visited[ni][nj] == 0:
                rear += 1
                q[rear] = (ni, nj)
                visited[ni][nj] = visited[i][j] + 1
    maxV = 0
    for i in range(N):
        for j in range(M):
            if maxV < visited[i][j]:
                maxV = visited[i][j]
            elif box[i][j] != -1 and visited[i][j] == 0:
                return -1
    return maxV - 1

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

print(bfs(N, M))