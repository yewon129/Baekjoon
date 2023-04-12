from collections import deque
from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def bfs(sti, stj, endi, endj):
    visited = [[0] * N for _ in range(N)]
    visited[sti][stj] = 1
    q = deque([])
    q.append([sti,stj])
    while q:
        i,j = q.popleft()
        if i == endi and j == endj:
            return visited[i][j]-1
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
                q.append([ni,nj])
                visited[ni][nj] = visited[i][j] + 1

cnt = 1
houses = []
chickens = []
for i in range(N):
    minV = [1000000, 0]
    for j in range(N):
        if arr[i][j] == 1:
            houses.append([i,j])
        elif arr[i][j] == 2:
            chickens.append([i,j])

ans = 1000000000

for chick in combinations(chickens, M):
    temp = 0
    for h in houses:
        minV = 1000000
        for k in chick:
            distance = abs(h[0]-k[0]) + abs(h[1]-k[1])
            if distance < minV:
                minV = distance
        temp += minV
    if ans > temp:
        ans = temp
print(ans)