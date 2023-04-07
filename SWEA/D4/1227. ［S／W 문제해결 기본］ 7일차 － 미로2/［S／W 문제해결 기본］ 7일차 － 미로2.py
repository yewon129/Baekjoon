def findst():
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                return i, j

def bfs(sti, stj):
    visited = [[0]*100 for _ in range(100)]
    visited[sti][stj] = 1
    q = [[sti, stj]]
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<100 and 0<=nj<100 and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append([ni,nj])
    return 0

for t in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    sti, stj = findst()
    
    answer = bfs(sti,stj)
    print(f'#{tc} {answer}')