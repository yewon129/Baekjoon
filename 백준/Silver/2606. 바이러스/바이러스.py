N = int(input())
M = int(input())

lst = [[0] * (N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    lst[a][b] = b
    lst[b][a] = a

cnt = 0

def dfs(s):
    global cnt
    v = [0] * (N+1)
    v[s] = 1
    stack = [s]
    while stack:
        k = stack.pop()
        for i in lst[k]:
            if i != 0 and v[i] == 0:
                v[i] = 1
                stack.append(i)
                cnt += 1

dfs(1)
print(cnt)