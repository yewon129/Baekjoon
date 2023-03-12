N ,M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
v = [0] * N
box = []

def dfs():
    if len(box) == M:
        print(*box)
        return
    temp = 0
    for i in range(N):
        if v[i] == 0 and temp != lst[i]:
            v[i] = 1
            box.append(lst[i])
            temp = lst[i]
            dfs()
            v[i] = 0
            box.pop()

dfs()