N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]
answer = 0
arr[0][0] = 1
d = [[0,1], [1,0], [0,-1], [-1,0]]
l = 0
i,j = 0,0
while 1:
    ni, nj = i+d[l][0], j+d[l][1]
    if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
        arr[ni][nj] = 1
        i, j = ni, nj
    else:
        l = (l+1)%4
        ni, nj = i+d[l][0], j+d[l][1]
        if arr[ni][nj] == 1:
            break
        else:
            answer += 1
print(answer)