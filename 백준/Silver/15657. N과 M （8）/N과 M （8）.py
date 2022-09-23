N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

ans = []

def dfs(k):
    if k == M:
        for i in range(len(ans)):
            print(ans[i], end=' ')
        print()
        return
    for i in range(N):
        if k == 0 or ans[k-1] <= lst[i]:
            ans.append(lst[i])
            dfs(k+1)
            ans.pop()

dfs(0)