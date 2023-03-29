N = int(input())
X, Y = map(int, input().split())
M = int(input())

lst = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    lst[x][y] = y
    lst[y][x] = x


def bfs(s):
    v = [0] * (N + 1)
    queue = [s]
    while queue:
        i = queue.pop(0)
        if i == Y:
            return v[i]
        for k in lst[i]:
            if k != 0 and v[k] == 0:
                v[k] = v[i] + 1
                queue.append(k)
    return -1

answer = bfs(X)
print(answer)