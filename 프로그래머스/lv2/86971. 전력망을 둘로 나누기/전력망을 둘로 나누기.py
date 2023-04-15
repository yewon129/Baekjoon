def solution(n, wires):
    answer = -1
    arr = [[] for _ in range(n+1)]
    for wire in wires:
        arr[wire[0]].append(wire[1])
        arr[wire[1]].append(wire[0])

    def bfs(st):
        cnt = 1
        visited = [0]*(n+1)
        q = [st]
        visited[st] = 1
        while q:
            i = q.pop(0)
            for k in arr[i]:
                if visited[k] == 0:
                    cnt += 1
                    q.append(k)
                    visited[k] = visited[i] + 1
        return cnt
    
    minV = 100000000
    for a,b in wires:
        arr[a].remove(b)
        arr[b].remove(a)
        cnt = bfs(a)
        if minV > abs(cnt-(n-cnt)):
            minV = abs(2*cnt - n)
        arr[a].append(b)
        arr[b].append(a)
        
    return minV