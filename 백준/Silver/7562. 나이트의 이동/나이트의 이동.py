from collections import deque
T = int(input())

def bfs(sti, stj):
    v = [[0]*N for _ in range(N)]
    q = deque([])
    q.append([sti, stj])
    v[sti][stj] = 1
    while q:
        i, j = q.popleft()
        if i == eni and j == enj:
            return v[i][j]-1
        for di, dj in [[-2, -1], [-1,-2], [1,-2], [2,-1], [2,1], [1,2], [-1,2],[-2, 1]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0:
                q.append([ni,nj])
                v[ni][nj] = v[i][j] + 1

for tc in range(T):
    N = int(input())
    sti, stj = map(int, input().split())
    eni, enj = map(int, input().split())

    ans = bfs(sti, stj)
    print(ans)