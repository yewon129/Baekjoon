def dfs(depth, idx):
    if depth == 6:
        print(*s)
        return
    for i in range(idx, k):
        s.append(lst[i])
        dfs(depth+1, i+1)
        s.pop()

while 1:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    k = lst[0]
    del lst[0]
    s = []
    dfs(0, 0)
    print()