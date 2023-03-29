N, K = map(int, input().split())
lst = [0] * 100001
def bfs(sti):
    queue = [sti]
    while queue:
        i = queue.pop(0)
        if i == K:
            return lst[i]
        for ni in [i-1, i+1, i*2]:
            if 0<=ni<=100000 and lst[ni] == 0:
                queue.append(ni)
                lst[ni] = lst[i] + 1

print(bfs(N))