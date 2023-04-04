from collections import deque

def bfs(sti,stj, counts):
    visited = [[0] * N for _ in range(N)]
    visited[sti][stj] = 1
    q = deque([[sti, stj]])
    while q:
        i, j = q.popleft()
        for di, dj in [[0,1], [1,0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    counts[ni][nj] = counts[i][j] + arr[ni][nj]
                    q.append([ni,nj])
                else:
                    if ni == 0 and nj == 0:
                        continue
                    elif counts[ni][nj] > counts[i][j] + arr[ni][nj]:
                        counts[ni][nj] = counts[i][j] + arr[ni][nj]
                        q.append([ni, nj])
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    counts = [[0] * N for _ in range(N)]
    bfs(0,0, counts)

    print(f'#{tc} {counts[N-1][N-1]}')