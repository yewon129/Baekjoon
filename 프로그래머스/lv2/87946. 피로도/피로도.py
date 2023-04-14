maxV = 0
v = []
N = 0

def solution(k, dungeons):
    global maxV, v, N
    N = len(dungeons)
    v = [0] * N
    maxV = 0
    # k : 현재 피로도, i : 던전 idx, n: 돌았던 갯수
    def dfs(k, i, n):
        global maxV
        if maxV < n:
            maxV = n
        for j in range(N):
            if k >= dungeons[j][0] and v[j] == 0:
                v[j] = 1
                dfs(k-dungeons[j][1], j, n+1)
                v[j] = 0
        
    dfs(k, 0, 0)
    return maxV