def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0] * m for _ in range(n)]
    
    def bfs(sti,stj):
        visited[sti][stj] = 1
        stack = [[sti,stj]]
        while stack:
            i, j = stack.pop(0)
            if i == n-1 and j == m-1:
                return visited[i][j]
            for di, dj in [[0, 1], [1,0], [0, -1], [-1,0]]:
                ni, nj = i+di, j+dj
                if 0<=ni<n and 0<=nj<m and maps[ni][nj] == 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    stack.append([ni,nj])
        return -1
    answer = bfs(0,0)
    return answer