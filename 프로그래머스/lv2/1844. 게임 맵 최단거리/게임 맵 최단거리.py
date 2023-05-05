from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    def bfs():
        v = [[0]*m for _ in range(n)]
        v[0][0] = 1
        q = deque([])
        q.append([0,0])
        while q:
            i, j = q.popleft()
            if i == n-1 and j == m-1:
                return v[i][j]
            for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
                ni , nj = i+di, j+dj
                if 0<=ni<n and 0<=nj<m and v[ni][nj] == 0 and maps[ni][nj] == 1:
                    q.append([ni,nj])
                    v[ni][nj] = v[i][j] + 1
        return -1
    answer = bfs()
    return answer