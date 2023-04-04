def findst(arr):
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                return i, j

def bfs(sti, stj):
    visited = [[0]*16 for _ in range(16)]
    visited[sti][stj] == 1
    q = [(sti,stj)]
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return 1
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<16 and 0<=nj<16 and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
    return 0

for t in range(1, 11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    sti, stj = findst(maze)
    
    answer = bfs(sti, stj)

    print(f'#{tc} {answer}')