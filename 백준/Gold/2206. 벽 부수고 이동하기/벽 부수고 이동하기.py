from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

v = [[[0]*2 for _ in range(M)] for _ in range(N)]

def bfs(sti, stj):
  global v
  v[sti][stj][0] = 1
  q = deque()
  q.append([sti, stj, 0])
  while q:
    i, j, w = q.popleft()
    if i == N-1 and j == M-1:
      return v[i][j][w]
    for di, dj in [[0,1], [1, 0], [0, -1], [-1, 0]]:
      ni, nj = i+di, j+dj
      if 0<=ni< N and 0<=nj<M:
        if arr[ni][nj] == 0 and v[ni][nj][w] == 0:
          q.append([ni, nj, w])
          v[ni][nj][w] = v[i][j][w] + 1
        elif arr[ni][nj] == 1 and w == 0:
            q.append([ni,nj, w+1])
            v[ni][nj][w+1] = v[i][j][w] + 1
  return -1

print(bfs(0,0))