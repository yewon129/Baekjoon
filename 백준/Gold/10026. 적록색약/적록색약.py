import sys
from collections import deque

N = int(sys.stdin.readline())
arr = [list(map(str, sys.stdin.readline())) for _ in range(N)]

def bfs(arr, sti, stj, k):
    q = deque()
    v = [[0] * N for _ in range(N)]
    q.append((sti, stj))
    v[sti][stj] = 1
    while q:
        i, j = q.popleft()
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and arr[ni][nj] == k:
                v[ni][nj] = v[i][j] +1
                q.append((ni,nj))
                arr[ni][nj] = 0

arr_rg = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr_rg[i][j] = 'R'
        else:
            arr_rg[i][j] = arr[i][j]

cnt = 0
cnt_rg = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            cnt += 1
            bfs(arr, i, j, arr[i][j])
        if arr_rg[i][j] != 0:
            cnt_rg +=1
            bfs(arr_rg, i, j, arr_rg[i][j])

print(cnt, cnt_rg)