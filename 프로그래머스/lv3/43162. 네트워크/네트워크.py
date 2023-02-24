def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def bfs(i):
        visited[i] = 1
        q = []
        q.append(i)
        while q:
            com = q.pop(0)
            for j in range(n):
                if computers[com][j] == 1 and visited[j] == 0:
                    q.append(j)
                    visited[j] = 1
    
    for k in range(n):
        if visited[k] == 0:
            bfs(k)
            answer += 1
    
    return answer