def solution(n):
    box = [[0] * i for i in range(1, n+1)]
    d = [[1,0], [0,1],[-1,-1],[0,-1]]
    N = 0
    for i in range(1,n+1):
        N += i
    answer = []
    k = 1
    dn = 0
    i = 0
    j = 0
    while 1:
        box[i][j] = k
        k += 1
        if k == N+1:
            break
        while 1:
            di, dj = d[dn]
            ni, nj = i+di, j+dj           
            if 0<=ni<n and 0<=nj<len(box[ni]) and box[ni][nj] == 0:
                i, j = ni, nj
                break
            else:
                dn = (dn+1) % 4
    
    for i in range(n):
        for j in range(len(box[i])):
            answer.append(box[i][j])
    return answer

