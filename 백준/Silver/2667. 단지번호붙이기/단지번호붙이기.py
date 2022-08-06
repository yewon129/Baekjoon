N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

box=[]
def bfs(sti, stj):
    global v
    cnt = 1
    q = [(sti,stj)]
    v[sti][stj] = 1
    while q:
        i, j = q.pop(0)
        for di,dj in [(0,1), (1,0), (-1,0), (0,-1)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and arr[ni][nj] != 0:
                q.append((ni,nj))
                v[ni][nj] = v[i][j] + 1
                cnt += 1

    box.append(cnt)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            v = [[0] * N for _ in range(N)]
            bfs(i,j)
            for x in range(N):
                for y in range(N):
                    if v[x][y] != 0:
                        arr[x][y] = 0

box.sort()
print(len(box))
for i in box:
    print(i)