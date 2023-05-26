from collections import deque
import sys
input = sys.stdin.readline


M, N, H = map(int, input().split())
lst = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

v = [[[0]* M for _ in range(N)] for _ in range(H)]
d = [[-1,0,0], [1,0,0], [0,1,0], [0,0,1], [0,-1,0], [0,0,-1]]
q = deque([])
def bfs():
    while q:
        h, i, j = q.popleft()
        for dh, di, dj in d:
            nh, ni, nj = h+dh, i+di, j+dj
            if 0<=nh<H and 0<=ni<N and 0<=nj<M and lst[nh][ni][nj] == 0 and v[nh][ni][nj] == 0:
                q.append([nh,ni,nj])
                lst[nh][ni][nj] = lst[h][i][j] + 1
                v[nh][ni][nj] = 1



for h in range(H):
    for i in range(N):
        for j in range(M):
            if lst[h][i][j] == 1:
                q.append([h,i,j])
                v[h][i][j] = 1

bfs()

day = 0
for h in lst:
    for i in h:
        for j in i:
            if j == 0:
                print(-1)
                exit(0)
        day = max(day, max(i))

print(day-1)