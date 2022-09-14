n, m = map(int, input().split())

s = []
def dfs(sti):
    if len(s) == m:
        for i in s:
            print(i, end=' ')
        print()
        return
    for j in range(sti, n+1):
        s.append(j)
        dfs(j)
        s.pop()

dfs(1)