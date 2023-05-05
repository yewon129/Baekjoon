def solution(n, computers):
    answer = 0
    v = [0] * n
    def bfs(i):
        q = [i]
        v[i] = 1
        while q:
            com = q.pop(0)
            for j in range(n):
                if computers[com][j] == 1 and v[j] == 0:
                    v[j] = 1
                    q.append(j)
    
    for i in range(n):
        if v[i] == 0:
            bfs(i)
            answer += 1
    return answer