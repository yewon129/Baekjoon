N, M = map(int, input().split())
lst = list(map(int, input().split()))

box = set(lst)
lst = list(box)
lst.sort()

def dfs(i):
    if i == M:
        for k in range(M):
            print(arr[k], end = ' ')
        print()
        return
    for j in range(len(lst)):
        if i == 0 or arr[-1] <= lst[j]:
            arr.append(lst[j])
            dfs(i+1)
            arr.pop()
arr = []
dfs(0)